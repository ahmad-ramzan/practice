from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import json
import re

app = Flask(__name__)

app_keywords = {
    "judge.me": "Judge.me Reviews",
"klaviyo": "Klaviyo",
"yotpo": "Yotpo Reviews",
"tawk.to": "Tawk.to Live Chat",
"privy": "Privy - Pop Ups & Email",
"loox": "Loox Reviews",
"rechargeapps": "Recharge Subscriptions",
"mailchimp": "Mailchimp Integration",
"bold": "Bold Apps",
"shopify-apps.s3": "Shopify App Store Integration",
"boostcommerce": "Boost Product Filter & Search",
"gorgias": "Gorgias - Customer Support",
"hotjar": "Hotjar - Analytics",
"zendesk": "Zendesk Chat & Support",
"omnisend": "Omnisend Email Marketing",
"limespot": "LimeSpot Personalizer",
"instafeed": "Instafeed - Instagram Feed",
"shopify_product_reviews": "Shopify Product Reviews",
"shopify-product-reviews": "Shopify Product Reviews",
"powr.io": "POWR Plugins",
"trustpilot": "Trustpilot Reviews",
"pagefly": "PageFly - Landing Page Builder",
"shogun": "Shogun Page Builder",
"webkul": "Webkul Multi-Vendor Marketplace",
"shopify_email": "Shopify Email",
"shopify-email": "Shopify Email",
"stamped.io": "Stamped.io Reviews",
"upsell": "Upsell and Cross-Sell",
"flexify": "Flexify Facebook Product Feed",
"pushowl": "PushOwl - Web Push Notifications",
"refersion": "Refersion Affiliate Marketing",
"judgeme": "Judge.me Product Reviews",
"aftership": "AfterShip Order Tracking",
"socialphotos": "Social Photos",
"printful": "Printful",
"kitcrm": "Kit - Marketing Automation",
"tracktor": "Tracktor Order Tracking",
"smartrmail": "SmartrMail",
"retargetapp": "RetargetApp",
"seo-manager": "SEO Manager",
"shopify_local_delivery": "Shopify Local Delivery",
"shopify-local-delivery": "Shopify Local Delivery",
"pluginseo": "Plug in SEO",
"shipstation": "ShipStation Integration",
"taxjar": "TaxJar",
"referralsaasquatch": "Referral SaaSquatch",
"fbmessenger": "Messenger Channel",
"snapchat_ads": "Snapchat Ads",
"snapchat-ads": "Snapchat Ads",
"google_channel": "Google Shopping",
"facebook_channel": "Facebook Channel",
"google-channel": "Google Shopping",
"facebook-channel": "Facebook Channel",
"adroll": "AdRoll Retargeting",
"trustbadge": "Trustbadge",
"paywhirl": "PayWhirl Recurring Payments",
"shippo": "Shippo Shipping Integration",
"multilingual_shopify": "Langify - Multilingual Store",
"multilingual-shopify": "Langify - Multilingual Store",
"transcy": "Transcy",
"translate_and_adapt": "Translate and Adapt",
"translate-and-adapt": "Translate and Adapt",
"wishlist": "Wishlist Plus",
"smartsearch": "Smart Search & Instant Search",
"sales_popup": "Sales Popups",
"sales-popup": "Sales Popups",
"instant_search_plus": "Instant Search Plus",
"instant-search_plus": "Instant Search Plus",
"rewind": "Rewind Backups",
"luckyorange": "Lucky Orange - Heatmaps & Replays",
"sales_notify": "Sales Notification",
"privy_popup": "Privy - Popup Conversion",
"privy-popup": "Privy - Popup Conversion",
"trackify": "Trackify X Facebook Pixel",
"spreadr": "Spreadr Amazon Importer",
"shopify_ping": "Shopify Ping",
"dser": "DSers - AliExpress Dropshipping",
"oberlo": "Oberlo Dropshipping",
"printify": "Printify - Print on Demand",
"viahub": "Vitals",
"wheelio": "Wheelio",
"smile_io": "Smile.io - Loyalty & Rewards",
"smile-io": "Smile.io - Loyalty & Rewards",
"globo": "Globo Mega Menu",
"herobuilder": "Hero Image Slider",
"powerbuy": "Power Buy",
"wholesale_club": "Wholesale Club",
"wholesale-club": "Wholesale Club",
"groovejar": "GrooveJar",
"apps.shopifycdn.com": "Shopify CDN Apps",
"listrak": "Listrak Marketing",
"trugento": "Trugento",
"feed_for_google_shopping": "Feed for Google Shopping",
"feed-for-google-shopping": "Feed for Google Shopping",
"redirectly": "Redirectly",
"connected_inventory": "Connected Inventory",
"connected-inventory": "Connected Inventory",
"zapiet": "Zapiet - Store Pickup + Delivery",
"pixel_manager": "Pixel Manager for Facebook",
"pixel-manager": "Pixel Manager for Facebook",
"seguno": "Seguno: Email Marketing",
"easyship": "Easyship - Shipping Automation",
"swell_rewards": "Swell Rewards",
"swell-rewards": "Swell Rewards",
"avada.io": "AVADA Marketing Automation",
"omni": "Omnisend",
"feedback_whiz": "FeedbackWhiz",
"feedback-whiz": "FeedbackWhiz",
"super_listrak": "Listrak Super",
"super-listrak": "Listrak Super",
"facebook_pixel": "Facebook Pixel Integration",
"facebook-pixel": "Facebook Pixel Integration",
"social_login": "Social Login",
"social-login": "Social Login",
"chatra": "Chatra Live Chat",
"quick_view": "Quick View by Secomapp",
"quick-view": "Quick View by Secomapp",
"reconvert": "ReConvert Upsell & Cross Sell",
"product_bundle": "Bundler Product Bundles",
"product-bundle": "Bundler Product Bundles", 
"currency_converter": "Currency Converter Plus",
"currency-converter": "Currency Converter Plus",
"shopify_flow": "Shopify Flow",
"shopify-flow": "Shopify Flow",
"gift_cards": "Gift Cards Suite",
"gift-cards": "Gift Cards Suite",
"recharge": "Recharge - Recurring Billing",
"dropified": "Dropified",
"shopify_theme": "Shopify Theme Customizer",
"shopify-theme": "Shopify Theme Customizer",
"beaconstac": "Beaconstac QR Code Generator",
"shoppable": "Shoppable Product",
"orderhive": "Orderhive - Inventory Management",
"growthtools": "Growth Tools",
"easy_dashboard": "Easy Dashboard",
"easy-dashboard": "Easy Dashboard",
"mailerlite": "MailerLite Email Marketing",
"sendinblue": "SendinBlue Email Marketing",
"afterpay": "Afterpay",
"affirm": "Affirm Payment Gateway",
"braintree": "Braintree Payment Gateway",
"stripe": "Stripe Payments",
"paypal": "PayPal Payments",
"authorize.net": "Authorize.Net Payments",
"klarna": "Klarna Payment Gateway",
"paymentwall": "Paymentwall",
"quadpay": "QuadPay",
"zipmoney": "ZipMoney",
"klarna_checkout": "Klarna Checkout",
"klarna-checkout": "Klarna Checkout",
"worldpay": "WorldPay Payment Gateway",
"checkout_com": "Checkout.com Payment Gateway",
"checkout-com": "Checkout.com Payment Gateway",
"paymill": "Paymill",
"payoneer": "Payoneer Payment Gateway",
"sezzle": "Sezzle Payments",
"stripe_3ds": "Stripe 3D Secure",
"stripe-3ds": "Stripe 3D Secure",
"payza": "Payza Payment Gateway",
"alipay": "Alipay",
"wepay": "WePay Payments",
"paytm": "Paytm Payment Gateway",
"payu": "PayU Payments",
"razorpay": "Razorpay Payments",
"splitit": "Splitit",
"ordermark": "Ordermark",
"tap_checkout": "Tap Checkout",
"tap-checkout": "Tap Checkout",
"codat": "Codat API Integration",
"adyen": "Adyen Payment Gateway",
"moovweb": "Moovweb Mobile Optimization",
"shopify_pos": "Shopify POS",
"shopify-pos": "Shopify POS",
"recharge_payments": "Recharge Payments",
"recharge-payments": "Recharge Payments",
"quickbooks": "QuickBooks Integration",
"xero": "Xero Accounting Integration",
"zendesk_chat": "Zendesk Chat Support",
"zendesk-chat": "Zendesk Chat Support",
"pipedrive": "Pipedrive CRM",
"hubspot": "HubSpot CRM",
"freshdesk": "Freshdesk Customer Support",
"intercom": "Intercom Support",
"zoho_crm": "Zoho CRM",
"zoho-crm": "Zoho CRM",
"activecampaign": "ActiveCampaign Email Marketing",
"drift": "Drift Live Chat",
"tidio": "Tidio Live Chat",
"livechat": "LiveChat Support",
"freshchat": "Freshchat Live Chat",
"gainsight": "Gainsight Customer Success",
"moosend": "Moosend Email Marketing",
"omnisend_marketing": "Omnisend Marketing",
"omnisend-marketing": "Omnisend Marketing",
"convertflow": "ConvertFlow Marketing Automation",
"mailchimp_marketing": "Mailchimp Marketing",
"mailchimp-marketing": "Mailchimp Marketing",
"kameleoon": "Kameleoon Personalization",
"scalefast": "Scalefast",
"subscibe_pro": "Subscribe Pro",
"subscibe-pro": "Subscribe Pro",
"easypop": "EasyPop - Pop Ups",
"surveys": "Survey Anyplace",
"quizify": "Quizify - Product Quizzes",
"primo": "Primo - Marketing Automation",
"pickfu": "PickFu - Product Polls",
"adext": "Adext AI Advertising",
"algolia": "Algolia Search",
"shopify_search": "Shopify Search",
"shopify-search": "Shopify Search",
"crosssell": "Cross Sell",
"google_analytics": "Google Analytics Integration",
"google-analytics": "Google Analytics Integration",
"helicopter": "Helicopter App",
"clickfunnels": "ClickFunnels",
"emailcapture": "Email Capture",
"mailmunch": "MailMunch Popups",
"privy_popups": "Privy Popups",
"privy-popups": "Privy Popups",
"sumome": "SumoMe",
"optinmonster": "OptinMonster",
"leadpages": "LeadPages",
"convertkit": "ConvertKit Email Marketing",
"constantcontact": "Constant Contact Email Marketing",
"moosend_email": "Moosend Email Automation",
"moosend-email": "Moosend Email Automation"
}

def fetch_shopify_store_data(store_url):
    if not store_url.startswith("http"):
        store_url = "https://" + store_url

    try:
        # Step 1: Fetch HTML Source
        response = requests.get(store_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Step 2: Try Extracting Theme Name from Meta or Inline Script
        theme_name = None
        for meta in soup.find_all("meta"):
            if 'theme' in meta.get('name', '').lower():
                theme_name = meta.get("content")
                break

        if not theme_name:
            for script in soup.find_all("script"):
                if script.string and "theme_store_id" in script.string:
                    match = re.search(r'Shopify\.theme\s*=\s*({.*?});', script.string.strip())
                    if match:
                        json_string = match.group(1)
                        try:
                            json_data = json.loads(json_string)
                            if "schema_name" in json_data and json_data["schema_name"]:
                                theme_name = json_data["schema_name"]
                            else:
                                theme_name = json_data.get("name", "Unknown")
                        except json.JSONDecodeError as e:
                            print("Error parsing JSON:", e)

        # Step 3: Extract App Widgets
        app_widgets = []
        for script in soup.find_all("script"):
            if script.get("src"):
                script_url = script["src"]
                for keyword, app_name in app_keywords.items():
                    if keyword in script_url.lower():
                        app_widgets.append(app_name)
            else:
                script_content = script.string
                if script_content:
                    for keyword, app_name in app_keywords.items():
                        if keyword in script_content.lower():
                            app_widgets.append(app_name)

        # Step 4: Fetch Products
        products_url = store_url.rstrip("/") + "/products.json"
        products_data = None
        try:
            products_response = requests.get(products_url)
            if products_response.status_code == 200:
                products_data = products_response.json()
        except requests.RequestException:
            pass

        # Return Data
        return {
            "theme_name": theme_name or "Not Found",
            "app_widgets": app_widgets or "No Known Apps Detected",
            "products_sample": products_data.get("products", [])[:5] if products_data else "No Products Found",
        }

    except requests.RequestException as e:
        return {"error": str(e)}

# Define the API route
@app.route('/fetch_shopify_store_data', methods=['GET'])
def api_fetch_shopify_store_data():
    # Define the store URL directly
    store_url = "maguireshoes.com"
    
    # Sanitize the input (in case you want to ensure correctness)
    if not store_url.startswith("http"):
        store_url = "https://" + store_url

    # Fetch data
    store_data = fetch_shopify_store_data(store_url)
    return jsonify(store_data)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, port=5001)
    # app.run(host='0.0.0.0', port=5001, debug=True)