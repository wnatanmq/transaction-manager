from transaction.transations_migration  import transaction_migration_handler    as tmh
from customer.customer_migration        import customer_migration_handler       as cmh
from dotenv                             import load_dotenv


def main():
    tmh()
    cmh()
    
if __name__ == "__main__":
    load_dotenv()
    print(__name__)
    main()