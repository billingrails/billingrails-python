"""
Billingrails API Client
"""

from typing import Any
import time
import requests

from .resources.accounts import AccountsResource
from .resources.credit_grants import CreditGrantsResource
from .resources.discounts import DiscountsResource
from .resources.events import EventsResource
from .resources.fees import FeesResource
from .resources.invoices import InvoicesResource
from .resources.meters import MetersResource
from .resources.payments import PaymentsResource
from .resources.payment_links import PaymentLinksResource
from .resources.checkout_sessions import CheckoutSessionsResource
from .resources.subscriptions import SubscriptionsResource
from .resources.products import ProductsResource
from .resources.plans import PlansResource
from .resources.prices import PricesResource
from .resources.tax_rates import TaxRatesResource

DEFAULT_TIMEOUT = 30
DEFAULT_MAX_RETRIES = 3


class Billingrails:
    """Billingrails API client with nested resource namespaces"""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.billingrails.com",
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES
    ):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        })
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

        # Top-level resources
        self.accounts = AccountsResource(self)
        self.payments = PaymentsResource(self)
        self.payment_links = PaymentLinksResource(self)
        self.checkout_sessions = CheckoutSessionsResource(self)

        self.subscriptions = SubscriptionsResource(self)
        self.products = ProductsResource(self)
        self.fees = FeesResource(self)
        self.prices = PricesResource(self)
        self.plans = PlansResource(self)
        self.events = EventsResource(self)
        self.meters = MetersResource(self)
        self.invoices = InvoicesResource(self)

        self.credit_grants = CreditGrantsResource(self)
        self.discounts = DiscountsResource(self)
        self.tax_rates = TaxRatesResource(self)

    def request(self, method: str, path: str, **kwargs) -> Any:
        """Make an HTTP request with retry logic"""
        url = f"{self.base_url}{path}"
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout

        last_exception = None
        for attempt in range(self.max_retries):
            try:
                response = self.session.request(method, url, **kwargs)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                  # Exponential backoff
                    time.sleep(2 ** attempt)
                    continue
                raise

        if last_exception:
            raise last_exception
