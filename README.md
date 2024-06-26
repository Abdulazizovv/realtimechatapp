
# Real time chat app

Real vaqt rejimida chat ilovasi




## Ilova ishga tushurish

1) Ilovani yuklab oling yoki shunchaki terminalda quyidagi buyruqni tering

```bash
    git clone https://github.com/Abdulazizovv/realtimechatapp.git
```

2) Yangi virtual muhit yarating
```bash
    python3 -m venv venv
```

agar python versiyangiz eskiroq bo'lsa

```bash
    python -m venv venv
```

3) Virtual muhitni aktivlashtiring

Windows:
```bash
    venv\Scripts\Activate
```

Linux: 
```bash
    venv/bin/activate
```

4) Kerakli kutubxonalarni o'rnating

```bash
pip install -r requirements.txt
```

5) Migratsiyalarni amalga oshiring
```bash
python3 manage.py migrate
```

6) Dasturni ishga tushurish
```bash
python3 manage.py runserver
```

