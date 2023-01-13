# email-sender-by-smtplib-advance-ways


- read emails from a text file and send them by smtp service.
- check operation time which is how much time it need for complete the script execution.

```
import smtplib
import ssl
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
from time import perf_counter
import json, os
from datetime import datetime
```

