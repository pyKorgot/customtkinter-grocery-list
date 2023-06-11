from app.core.db import update_migration
from app.main import AppController

if __name__ == "__main__":
    update_migration()
    app = AppController()
    app.mainloop()
