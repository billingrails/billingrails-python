# Billingrails Python SDK

Official Python SDK for [Billingrails](https://billingrails.com) - Flexible, composable, and intuitive API-first commerce platform.

## Installation

```bash
pip install billingrails
```

## Quick Start

```python
from billingrails import Billingrails

# Initialize the client
client = Billingrails(
    api_key="your-api-key",
    base_url="https://api.billingrails.com"
)

# List accounts
accounts = client.accounts.list()

# Create an account
account = client.accounts.create({
    "name": "John Doe",
    "email": "john@example.com",
    "country": "US",
    "default_currency": "USD"
})

# Retrieve an account
retrieved_account = client.accounts.retrieve("acc_123")

# Update an account
updated_account = client.accounts.update("acc_123", {
    "name": "Jane Doe"
})

# Get account balances
balances = client.accounts.get_balances("acc_123")

# Debit an account
debit_result = client.accounts.debit("acc_123", {
    "amount": 1000,  # Amount in cents
    "currency": "USD"
})
```

## Configuration

### Basic Configuration

```python
client = Billingrails(api_key="your-api-key")
```

### Advanced Configuration

```python
client = Billingrails(
    api_key="your-api-key",
    base_url="https://api.billingrails.com",
    timeout=30,  # Request timeout in seconds
    max_retries=3  # Maximum number of retries for failed requests
)
```

## API Resources

The SDK organizes resources into namespaces for better structure:

### Top-level Resources

- `client.accounts` - Account management
- `client.credit_grants` - Credit grant operations
- `client.discounts` - Discount management
- `client.fees` - Fee operations
- `client.invoices` - Invoice management
- `client.payments` - Payment operations
- `client.payment_pages` - Payment page management

### Biller Namespace

- `client.biller.events` - Event tracking
- `client.biller.meters` - Meter management
- `client.biller.plans` - Plan configuration
- `client.biller.subscriptions` - Subscription management

### Seller Namespace

- `client.seller.products` - Product catalog
- `client.seller.orders` - Order management

## Examples

### Working with Biller Resources

```python
# Create a subscription
subscription = client.biller.subscriptions.create({
    "account_id": "acc_123",
    "plan_id": "plan_456",
    "start_date": "2026-01-01"
})

# Track an event
event = client.biller.events.create({
    "account_id": "acc_123",
    "meter_id": "meter_789",
    "value": 100
})
```

### Working with Seller Resources

```python
# Create a product
product = client.seller.products.create({
    "name": "Premium Widget",
    "price": 9999,
    "currency": "USD"
})

# Create an order
order = client.seller.orders.create({
    "account_id": "acc_123",
    "product_id": product["id"],
    "quantity": 2
})
```

## Error Handling

```python
from billingrails import Billingrails
import requests

client = Billingrails(api_key="your-api-key")

try:
    account = client.accounts.retrieve("acc_123")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
```

## Development

```bash
# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black billingrails/
isort billingrails/

# Type checking
mypy billingrails/
```

## License

MIT
