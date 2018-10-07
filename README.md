# PlivoAssignment

### Two files are created where "functions.py" contains the fuctions for all six steps required to be done and "plivo_main.py" contains the execution logic


### get_number() Function:

```ini
To select any two number rented out to the account and return these two numbers
```

### send_message() Function:

```ini
To send message from one number to the other number selected above and return the message UUID to extract details
```

### get_message_details() Function:

```ini
Using the UUID above, find out the price deducted for the message
```

### get_pricing() Function:

```ini
Get the pricing decided for each message depending upon the country ISO(country_iso=US is used)
```

### compare_pricing() Function:

```ini
Verify whether the price deducted is equal to the outbound rate decided.
```

### get_account_details() Function:

```ini
Get the cash credit available to the account to verify that price deducted is less tan cash credit available
```

### Execution:

Both the files should be under same folder pre-execution. 

For execution:

```bash
python plivo_main.py
```


