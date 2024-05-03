SQLALCHEMY_DATABASE_URL = "sqllite:///../todo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmarker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

class Todo(Base):
    __tablename__ = "todos"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    decription = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    title: str
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@app.post("/todos/")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db_query(Todo).filter(Todo.id == todo_id),first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return db_todo

