import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("/Users/jackmurdock/Documents/sprint5-librarydb-firebase-adminsdk-fbsvc-81621e5243.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
authors_list = [
    {"id": "andrzej_sapkowski", "first_name": "Andrzej", "last_name": "Sapkowski", "birth_year": 1948, "death_year": None},
    {"id": "susanna_clarke", "first_name": "Susanna", "last_name": "Clarke", "birth_year": 1959, "death_year": None},
    {"id": "cs_lewis", "first_name": "C.S.", "last_name": "Lewis", "birth_year": 1898, "death_year": 1963},
    {"id": "norm_macdonald", "first_name": "Norm", "last_name": "Macdonald", "birth_year": 1959, "death_year": 2021},
    {"id": "terry_pratchett", "first_name": "Terry", "last_name": "Pratchett", "birth_year": 1948, "death_year": 2015},
    {"id": "john_gardner", "first_name": "John", "last_name": "Gardner", "birth_year": 1933, "death_year": 1982},
    {"id": "timothy_zahn", "first_name": "Timothy", "last_name": "Zahn", "birth_year": 1951, "death_year": None},
    {"id": "karen_traviss", "first_name": "Karen", "last_name": "Traviss", "birth_year": 1960, "death_year": None},
    {"id": "john_steakley", "first_name": "John", "last_name": "Steakley", "birth_year": 1951, "death_year": 2010},
    {"id": "william_goldman", "first_name": "William", "last_name": "Goldman", "birth_year": 1931, "death_year": 2018},
    {"id": "mark_twain", "first_name": "Mark", "last_name": "Twain", "birth_year": 1835, "death_year": 1910},
    {"id": "thomas_harris", "first_name": "Thomas", "last_name": "Harris", "birth_year": 1940, "death_year": None},
    {"id": "albert_camus", "first_name": "Albert", "last_name": "Camus", "birth_year": 1913, "death_year": 1960},
    {"id": "pg_wodehouse", "first_name": "P.G.", "last_name": "Wodehouse", "birth_year": 1881, "death_year": 1975},
    {"id": "george_rr_martin", "first_name": "George R.R.", "last_name": "Martin", "birth_year": 1948, "death_year": None},
    {"id": "thomas_pynchon", "first_name": "Thomas", "last_name": "Pynchon", "birth_year": 1931, "death_year": None},
    {"id": "jon_ronson", "first_name": "Jon", "last_name": "Ronson", "birth_year": 1967, "death_year": None},
    {"id": "jk_rowling", "first_name": "J.K.", "last_name": "Rowling", "birth_year": 1965, "death_year": None},
    {"id": "thomas_ligotti", "first_name": "Thomas", "last_name": "Ligotti", "birth_year": 1953, "death_year": None},
    {"id": "robert_w_chambers", "first_name": "Robert W.", "last_name": "Chambers", "birth_year": 1865, "death_year": 1933},
    {"id": "douglas_adams", "first_name": "Douglas", "last_name": "Adams", "birth_year": 1952, "death_year": 2001},
    {"id": "upton_sinclair", "first_name": "Upton", "last_name": "Sinclair", "birth_year": 1878, "death_year": 1968},
    {"id": "barbara_kingsolver", "first_name": "Barbara", "last_name": "Kingsolver", "birth_year": 1955, "death_year": None},
    {"id": "hp_lovecraft", "first_name": "Howard Philips", "last_name": "Lovecraft", "birth_year": 1890, "death_year": 1937},
    {"id": "cormac_mccarthy", "first_name": "Cormac", "last_name": "McCarthy", "birth_year": 1933, "death_year": 2023},
    {"id": "truman_capote", "first_name": "Truman", "last_name": "Capote", "birth_year": 1924, "death_year": 1984},
    {"id": "arthur_machen", "first_name": "Arthur", "last_name": "Machen", "birth_year": 1863, "death_year": 1947},
    {"id": "seamus_heaney", "first_name": "Seamus", "last_name": "Heaney", "birth_year": 1939, "death_year": 2013},
    {"id": "thomas_morton", "first_name": "Thomas", "last_name": "Morton", "birth_year": 1579, "death_year": 1647},
    {"id": "william_hope_hodgson", "first_name": "William Hope", "last_name": "Hodgson", "birth_year": 1877, "death_year": 1918},
    {"id": "anthony_burgess", "first_name": "Anthony", "last_name": "Burgess", "birth_year": 1917, "death_year": 1993}
]
books_list = [
    {"title": "The Sword of Destiny", "year": 2015, "pages": 384, "author_id": "andrzej_sapkowski"},
    {"title": "The Ladies of Grace Adieu", "year": 2006, "pages": 235, "author_id": "susanna_clarke"},
    {"title": "Mere Christianity", "year": 1952, "pages": 175, "author_id": "cs_lewis"},
    {"title": "Based on a True Story", "year": 2016, "pages": 272, "author_id": "norm_macdonald"},
    {"title": "Guards, Guards!", "year": 1989, "pages": 384, "author_id": "terry_pratchett"},
    {"title": "Wyrd Sisters", "year": 1988, "pages": 352, "author_id": "terry_pratchett"},
    {"title": "Grendel", "year": 1971, "pages": 174, "author_id": "john_gardner"},
    {"title": "Men At Arms", "year": 1993, "pages": 377, "author_id": "terry_pratchett"},
    {"title": "Heir to the Empire", "year": 1991, "pages": 474, "author_id": "timothy_zahn"},
    {"title": "Witches Abroad", "year": 1991, "pages": 384, "author_id": "terry_pratchett"},
    {"title": "Republic Commando", "year": 2004, "pages": 352, "author_id": "karen_traviss"},
    {"title": "Piranesi", "year": 2020, "pages": 272, "author_id": "susanna_clarke"},
    {"title": "Armor", "year": 1984, "pages": 432, "author_id": "john_steakley"},
    {"title": "The Princess Bride", "year": 1973, "pages": 493, "author_id": "william_goldman"},
    {"title": "Blood of Elves", "year": 2008, "pages": 320, "author_id": "andrzej_sapkowski"},
    {"title": "Huckleberry Finn", "year": 1885, "pages": 362, "author_id": "mark_twain"},
    {"title": "Hannibal", "year": 1999, "pages": 484, "author_id": "thomas_harris"},
    {"title": "The Stranger", "year": 1946, "pages": 159, "author_id": "albert_camus"},
    {"title": "The Inimitable Jeeves", "year": 1923, "pages": 256, "author_id": "pg_wodehouse"},
    {"title": "A Knight of the Seven Kingdoms", "year": 2015, "pages": 368, "author_id": "george_rr_martin"},
    {"title": "Time of Contempt", "year": 2013, "pages": 416, "author_id": "andrzej_sapkowski"},
    {"title": "Baptism of Fire", "year": 2014, "pages": 352, "author_id": "andrzej_sapkowski"},
    {"title": "Tower of Swallows", "year": 2016, "pages": 464, "author_id": "andrzej_sapkowski"},
    {"title": "Lady of the Lake", "year": 2017, "pages": 544, "author_id": "andrzej_sapkowski"},
    {"title": "The Crying of Lot 49", "year": 1966, "pages": 183, "author_id": "thomas_pynchon"},
    {"title": "Them: Adventures With Extremists", "year": 2001, "pages": 337, "author_id": "jon_ronson"},
    {"title": "The Men Who Stare At Goats", "year": 2004, "pages": 277, "author_id": "jon_ronson"},
    {"title": "Harry Potter & Sorcerer's Stone", "year": 1997, "pages": 223, "author_id": "jk_rowling"},
    {"title": "Songs of a Dead Dreamer", "year": 1985, "pages": 165, "author_id": "thomas_ligotti"},
    {"title": "Grimscribe", "year": 1991, "pages": 214, "author_id": "thomas_ligotti"},
    {"title": "The King In Yellow", "year": 1895, "pages": 151, "author_id": "robert_w_chambers"},
    {"title": "Restaurant at the End of the Universe", "year": 1980, "pages": 256, "author_id": "douglas_adams"},
    {"title": "Oil!", "year": 1927, "pages": 572, "author_id": "upton_sinclair"},
    {"title": "Harry Potter & Chamber of Secrets", "year": 1998, "pages": 341, "author_id": "jk_rowling"},
    {"title": "Demon Copperhead", "year": 2022, "pages": 560, "author_id": "barbara_kingsolver"},
    {"title": "The Call of Cthulhu", "year": 1999, "pages": 201, "author_id": "hp_lovecraft"},
    {"title": "No Country For Old Men", "year": 2005, "pages": 309, "author_id": "cormac_mccarthy"},
    {"title": "In Cold Blood", "year": 1966, "pages": 343, "author_id": "truman_capote"},
    {"title": "The Great God Pan", "year": 1894, "pages": 341, "author_id": "arthur_machen"},
    {"title": "Beowulf", "year": 1999, "pages": 144, "author_id": "seamus_heaney"},
    {"title": "The New English Canaan", "year": 1637, "pages": 386, "author_id": "thomas_morton"},
    {"title": "Inherent Vice", "year": 2009, "pages": 384, "author_id": "thomas_pynchon"},
    {"title": "The House on the Borderland", "year": 1908, "pages": 152, "author_id": "william_hope_hodgson"},
    {"title": "Season of Storms", "year": 2018, "pages": 384, "author_id": "andrzej_sapkowski"},
    {"title": "The Screwtape Letters", "year": 1942, "pages": 157, "author_id": "cs_lewis"},
    {"title": "A Clockwork Orange", "year": 1962, "pages": 176, "author_id": "anthony_burgess"}
]
def library_setup():
    for author in authors_list:
        data = author.copy()
        doc_id = data.pop("id")
        db.collection("authors").document(doc_id).set(data)
    for book in books_list:
        db.collection("books").add(book)
    print("Library setup finished.")
def author_books(author_id):
    search_id = author_id.lower().replace(" ", "_")
    print (f"\nBooks by {author_id}:")
    books = db.collection("books").where(filter=FieldFilter("author_id", "==", search_id)).get()
    if books:
        for book in books:
            data = book.to_dict()
            print(f"{data['title']} - ({data['year']})")
    else:
        print("No books found :(")
def update_year(title, new_year):
    books = db.collection("books").where(filter=FieldFilter("title", "==", title)).limit(1).get()
    if len(books)>0:
        db.collection("books").document(books[0].id).update({"year": new_year})
        print (f"\nYear for {title} changed to {new_year}.")
    else:
        print(f"{title} not found.")
def delete_book(title):
    books = db.collection("books").where(filter=FieldFilter("title", "==", title)).get()
    for book in books: 
        db.collection("books").document(book.id).delete()
        print(f"\nDeleted: {title}")

print("Welcome to Library DB.")
if(len(db.collection("books").limit(1).get())== 0):
    print("\n Setting up database...")
    library_setup()
else:
    print("\n Database found!")
a = input("Type in the name of an author to find their books: ")
author_books(a)
print("\nLet's check out Beowulf.")
author_books("Seamus Heaney")
print("Whoops! Beowulf wasn't actually written then!!! (only this translation)")
update_year("Beowulf", 700)
print("You know what? Let's just get rid of it.")
delete_book("Beowulf")
author_books("Seamus Heaney")
print("That's better.")