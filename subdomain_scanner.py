import asyncio
import aiohttp
import aiodns
import dns.resolver
import json
from tqdm import tqdm
import concurrent.futures
import requests
from typing import List, Set, Dict
import logging
import platform
from datetime import datetime

class SubdomainScanner:
    def __init__(self, target_domain: str):
        self.target_domain = target_domain
        self.subdomains: Set[str] = set()
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('subdomain_scan.log'),
                logging.StreamHandler()
            ]
        )

    async def check_subdomain(self, subdomain: str) -> Dict:
        """Subdomain'in varlığını ve erişilebilirliğini kontrol eder."""
        full_domain = f"{subdomain}.{self.target_domain}"
        result_data = {
            "domain": full_domain,
            "status": "not_found",
            "ip_addresses": [],
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = self.resolver.resolve(full_domain, 'A')
            if result:
                result_data["status"] = "found"
                result_data["ip_addresses"] = [str(ip) for ip in result]
                self.subdomains.add(full_domain)
                logging.info(f"Bulunan subdomain: {full_domain}")
        except Exception as e:
            result_data["error"] = str(e)
        
        return result_data

    async def brute_force_scan(self, wordlist_file: str) -> List[Dict]:
        """Brute force yöntemiyle subdomain taraması yapar."""
        results = []
        try:
            with open(wordlist_file, 'r') as f:
                subdomains = f.read().splitlines()
        except FileNotFoundError:
            logging.error(f"Wordlist dosyası bulunamadı: {wordlist_file}")
            return results

        tasks = []
        for subdomain in tqdm(subdomains, desc="Brute Force Taraması"):
            task = asyncio.create_task(self.check_subdomain(subdomain))
            tasks.append(task)
            if len(tasks) >= 100:  # Rate limiting
                results.extend(await asyncio.gather(*tasks))
                tasks = []
        
        if tasks:
            results.extend(await asyncio.gather(*tasks))
        
        return results

    def get_crt_sh_subdomains(self) -> List[Dict]:
        """Certificate Transparency loglarından subdomain bilgisi çeker."""
        results = []
        url = f"https://crt.sh/?q=%.{self.target_domain}&output=json"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for entry in data:
                    name = entry['name_value'].lower()
                    if '*' not in name:
                        self.subdomains.add(name)
                        results.append({
                            "domain": name,
                            "source": "crt.sh",
                            "timestamp": datetime.now().isoformat()
                        })
                logging.info(f"crt.sh'den {len(data)} kayıt alındı")
        except Exception as e:
            logging.error(f"crt.sh sorgulaması sırasında hata: {str(e)}")
        
        return results

    def check_wildcard_dns(self) -> Dict:
        """Wildcard DNS yapılandırmasını kontrol eder."""
        result = {
            "has_wildcard": False,
            "timestamp": datetime.now().isoformat()
        }
        
        random_subdomain = f"wildcard_test_{''.join([str(x) for x in range(10)])}"
        try:
            self.resolver.resolve(f"{random_subdomain}.{self.target_domain}", 'A')
            result["has_wildcard"] = True
            logging.warning("Wildcard DNS yapılandırması tespit edildi!")
        except Exception as e:
            result["error"] = str(e)
        
        return result

    async def scan(self, wordlist_file: str = 'subdomains.txt') -> Dict:
        """Tüm tarama yöntemlerini çalıştırır."""
        logging.info(f"Tarama başlatılıyor: {self.target_domain}")
        
        scan_results = {
            "target_domain": self.target_domain,
            "scan_start": datetime.now().isoformat(),
            "wildcard_dns": self.check_wildcard_dns(),
            "crt_sh_results": self.get_crt_sh_subdomains(),
            "brute_force_results": await self.brute_force_scan(wordlist_file),
            "total_subdomains_found": len(self.subdomains),
            "scan_end": None
        }
        
        # Sonuçları metin dosyasına kaydet
        with open(f"{self.target_domain}_subdomains.txt", 'w') as f:
            for subdomain in sorted(self.subdomains):
                f.write(f"{subdomain}\n")
        
        # Sonuçları JSON formatında kaydet
        scan_results["scan_end"] = datetime.now().isoformat()
        with open(f"{self.target_domain}_results.json", 'w', encoding='utf-8') as f:
            json.dump(scan_results, f, indent=4, ensure_ascii=False)
        
        logging.info(f"Tarama tamamlandı. {len(self.subdomains)} subdomain bulundu.")
        return scan_results

async def main():
    domain = input("Hedef domain'i girin (örn: example.com): ")
    scanner = SubdomainScanner(domain)
    results = await scanner.scan()
    print("\nBulunan Subdomainler:")
    for subdomain in sorted(scanner.subdomains):
        print(subdomain)
    print(f"\nDetaylı sonuçlar {domain}_results.json dosyasına kaydedildi.")

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main()) 