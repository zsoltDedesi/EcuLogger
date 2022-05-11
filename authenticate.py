import data
import bcrypt



def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):

    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def check_password_hash(plain_text_password, username):    

    stored_pw = data.get_userpw_by_id(username)['password']
    return verify_password(plain_text_password, stored_pw)
   
def user_loged_in(user_id=None):
    
    if user_id is not None:
        
        print(f"You are loged in {user_id}")
        return True

    else:
        print(f'You are not logged in {user_id}')
        return False

        # return redirect('/register')

