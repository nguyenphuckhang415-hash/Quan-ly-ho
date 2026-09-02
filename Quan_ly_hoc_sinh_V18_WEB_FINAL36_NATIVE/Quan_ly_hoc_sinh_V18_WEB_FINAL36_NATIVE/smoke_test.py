import os, tempfile, sqlite3
from app import init_db, db, add_student_roster, assign, save_score, save_task

root=tempfile.mkdtemp(prefix="v18web-smoke-")
os.environ["V18_DATA_DIR"]=root
# app.DB_FILE is computed at import time; patch module globals for isolated test
import app
app.DATA_DIR=root; app.DB_FILE=os.path.join(root,"quan_ly_hoc_sinh.db"); app.UPLOAD_DIR=os.path.join(root,"uploads"); os.makedirs(app.UPLOAD_DIR, exist_ok=True)
init_db()
r=add_student_roster(name="Smoke User", class_name="6A1", team="Tổ 1", parent_name="PH Smoke", parent_email="smoke@example.com")
assert r["ok"] and r["student_id"]
sid=r["student_id"]
assert save_score(sid, "Toán", 9)["ok"]
assert save_task(sid, "Ôn bài", "Ghi chú", "2026-09-02")["ok"]
assert assign(sid, title="Bài tập", task_date="2026-09-03")["ok"]
c=db(); assert c.execute("SELECT criterion,points FROM scores WHERE student_id=?",(sid,)).fetchone()==("Toán",9) if False else True
sc=c.execute("SELECT criterion,points FROM scores WHERE student_id=?",(sid,)).fetchone(); assert sc[0]=="Toán" and sc[1]==9
tasks=c.execute("SELECT COUNT(*) FROM tasks WHERE student_id=?",(sid,)).fetchone()[0]; assert tasks==2
par=c.execute("SELECT username,password_display,must_change FROM parents WHERE student_id=?",(sid,)).fetchone(); assert par and par[0] and par[1] and par[2]==1
c.close(); print("SMOKE_OK")
