from gcm import GCM
import argparse

# API Key for your Google OAuth project
API_KEY = ''


def send_push_notification(registration_id, message):
    gcm = GCM(API_KEY)
    resp = gcm.plaintext_request(registration_id=registration_id,
                                 data={'message': message})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reg-id', dest='registration_id', required=True)
    parser.add_argument('-m', '--message', dest='message', required=True)
    args = parser.parse_args()
    send_push_notification(args.registration_id, args.message)

