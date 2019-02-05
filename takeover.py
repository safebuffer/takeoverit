
from requests import get
from multiprocessing.dummy import Pool
import sys
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

try:
    if len(sys.argv) > 1:
        zerorg = sys.argv[1]
        zero = open(zerorg,'r').readlines()
    else:
        print(bcolors.FAIL + str('[-] Pass The List :) ') + bcolors.ENDC)
        exit()
except:
    pass
datas_one = [ "<strong>Trying to access your account",
                       "Use a personal domain name",
                        "The request could not be satisfied",
                        "Sorry, We Couldn't Find That Page",
                        "Fastly error: unknown domain",
                        "The feed has not been found",
                        "herokucdn.com/error-pages/no-such-app.html",
                        "The gods are wise, but do not know of the site which you seek",
                        "Whatever you were looking for doesn't currently exist at this address",
                        "Sorry, We Couldn't Find That Page",
                        "Help Center Closed",
                        "Oops - We didn't find your site",
                        "We could not find what you're looking for",
                        "No settings were found for this company",
                        "The specified bucket does not exist",
                        "The thing you were looking for is no longer here",
                        "<title>404 &mdash; File not found</title>",
                        "The feed has not been found",
                        "Sorry, this shop is currently unavailable",
                        "You are being <a href=\"https://www.statuspage.io\">redirected",
                        "This UserVoice subdomain is currently available!",
                        "project not found",
			            "Nothing found for the requested URL",
                        "Repository not found",
                        "This page is reserved for artistic dogs",
                        "<p class=\"description\">The page you are looking for doesn't exist or has been moved.</p>",
                        "<h1>The page you were looking for doesn't exist.</h1>",
                        "You may have mistyped the address or the page may have moved",
                        "https://www.wishpond.com/404?campaign=true",
                        "Oops.</h2><p class=\"text-muted text-tight\">The page you're looking for doesn't exist",
                        "There is no portal here ... sending you back to Aha",
                        "to target URL: <a href=\"https://tictail.com",
                        "Start selling on Tictail",
                        "<p class=\"bc-gallery-error-code\">Error Code: 404</p>",
                        "<h1>Oops! We couldn&#8217;t find that page.</h1>",
                        "LIGHTTPD - fly light",
                        "mailto:help@createsend.com",
                        "The site you are looking for could not be found.",
                        "mailto:support@proposify.biz",
                        "https://simplebooklet.com",
                        "With GetResponse Landing Pages, lead generation has never been easier",
                        "Looks like you've traveled too far into cyberspace",
                        "is not a registered InCloud YouTrack",
                        "You can claim it now at",
                        "Publishing platform",                        
                        "There isn't a GitHub Pages site here",
                        "<title>No such app</title>",                        
                        "No settings were found for this company",
                        "<title>No such app</title>",                        
                        "You've Discovered A Missing Link. Our Apologies!",
                        "Sorry, couldn&rsquo;t find the status page",                        
                        "NoSuchBucket",
                        "Sorry, this shop is currently unavailable",
                        "<title>Hosted Status Pages for Your Company</title>",
                        "data-html-name=\"Header Logo Link\"",                        
                        "<title>Oops - We didn't find your site.</title>",
                        "class=\"MarketplaceHeader__tictailLogo\"",                        
                        "Whatever you were looking for doesn't currently exist at this address",
                        "The requested URL was not found on this server",
                        "The page you have requested does not exist",
                        "This UserVoice subdomain is currently available!",
                        "Domain has been assigned",
                        "pingdom",
                        "Please check that this domain has been added to a service",
                        "If you are an Acquia Cloud customer and expect",
                        "Domain is not configured",
                        "Better Status Communication",
                        "Building a brand of your own?",
                        "Please try again or try Desk.com free for 14 days",
                        "You've Discovered A Missing Link. Our Apologies!",
                        "this shop is currently unavailable",
                        "Whatever you were looking for doesn't currently exist",
                        "The requested URL / was not found on this server",
                        "herokucdn.com/error-pages/no-such-app.html",
                        "The requested URL was not found on this server",
                        "but is not configured for an account on our platform",
                        "<title>Help Center Closed | Zendesk</title>"]


def star_(d):
    try:
        ht = get("http://{}".format(d)).text
        hts = get("https://{}".format(d)).text #just to make sure ! :)
        print(bcolors.OKBLUE + str('[*] Testing {}'.format(d)) + bcolors.ENDC)
        for rep in datas_one:
            if str(rep) in str(ht):
                print(bcolors.OKGREEN + str('[+] Takeover {}'.format(d)) + bcolors.ENDC)
                open('takeover.txt','a').write(q[0]+'\n')
            if str(rep) in str(ht):
                print(bcolors.OKGREEN + str('[+] Takeover {}'.format(d)) + bcolors.ENDC)
                open('takeover.txt','a').write(q[0]+'\n')
    except Exception as e:
        pass

def HelloZ():
    try:
        Theards = Pool(30)
        Theard = Theards.map(star_, zero)
        print("[+] Done Saved to takeover.txt")
    except Exception as e:
        pass

if __name__ == '__main__':
    HelloZ()