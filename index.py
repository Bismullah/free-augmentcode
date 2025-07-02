from augutils.json_modifier import reset_json_ids
from augutils.sqlite_modifier import clean_sqlite_database
from augutils.workspace_cleaner import clean_workspace

def main():
    print("🔧 Starting AugmentCode Cleaner...")

    reset_json_ids()
    clean_sqlite_database()
    clean_workspace()

    print("✅ All tasks completed!")

if __name__ == "__main__":
    main()
