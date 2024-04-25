from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database connection URI
db_uri = "sqlite:///new-books-collection.db"

# Create a SQLAlchemy engine
engine = create_engine(db_uri)

# Define a base class for declarative class definitions
Base = declarative_base()

# Define your database model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Float)

# Bind the engine to the Base class
Base.metadata.create_all(engine)

# Create a session class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example of adding data to the database
new_book = Book(title='Sample Book', author='John Doe', price=19.99)
session.add(new_book)
session.commit()

# Example of querying data from the database
books = session.query(Book).all()
for book in books:
    print(book.title, book.author, book.price)

# Close the session
session.close()

