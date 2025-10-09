import sqlite3

# 1. DB 연결 (파일이 없으면 'address.db' 자동 생성)
conn = sqlite3.connect('SQLite/address.db')

# 2. 커서 생성
c = conn.cursor()

# 3. SQL 실행: 'addressbook' 테이블 생성
# IF NOT EXISTS: 테이블이 이미 존재하면 오류 없이 넘어감 (안전장치)
c.execute('''
    CREATE TABLE IF NOT EXISTS addressbook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT UNIQUE
    )
''')

# 4. 변경사항 저장 (commit)
conn.commit()

# 5. 연결 종료
conn.close()

print("테이블이 성공적으로 생성되었습니다.")

# cwd = where you run the script from

# Doesn’t care where the .py file is saved