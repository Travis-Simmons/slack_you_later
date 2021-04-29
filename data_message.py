my_token = 

import slack
import argparse
# --------------------------------------------------
def get_args():
        """Get command-line arguments"""
        parser = argparse.ArgumentParser(
            description='message',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument('-m','--message',metavar='message',help='what message you want to send',type=str,required=True)

        return parser.parse_args()


# --------------------------------------------------
def main():
        args = get_args()


        client = slack.WebClient(token=my_token)
        client.chat_postMessage(channel='gantry_data_updates', text=args.message)


# --------------------------------------------------
if __name__ == '__main__':
        main()

