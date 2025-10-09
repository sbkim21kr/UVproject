import sqlite3

conn = sqlite3.connect('SQLite/address.db')
c = conn.cursor()

# [방법 1] 한 개의 데이터 추가 (안전한 방식)
# SQL Injection 공격을 방지하기 위해 반드시 플레이스홀더(?)를 사용해야 합니다.
name = '홍길동'
phone = '010-1111-2222'
email = 'gildong@example.com'
c.execute("INSERT INTO addressbook (name, phone, email) VALUES (?, ?, ?)", 
          (name, phone, email))

# [방법 2] 여러 데이터 한번에 추가
contacts = [
    ('이순신', '010-3333-4444', 'sunsin@example.com'),
    ('유관순', '010-5555-6666', 'gwansun@example.com')
]
c.executemany("INSERT INTO addressbook (name, phone, email) VALUES (?, ?, ?)", contacts)

conn.commit()
conn.close()

print("데이터가 성공적으로 추가되었습니다.")
