import os, time, json
from openwa import WhatsAPIDriver

config = json.loads(open("config.json", "r").read())
contact_B = "{}@c.us".format(config["contact_B"])
contact_A = "{}@c.us".format(config["contact_A"])

def run():
	driver = WhatsAPIDriver(client='chrome')
	print("Waiting for QR")
	driver.wait_for_login()
	print("Bot started")

	driver.subscribe_new_messages(NewMessageObserver(driver))
	print("Waiting for new messages...")

	while True:
		time.sleep(1)


class NewMessageObserver:
	def __init__(self, driver):
		self.driver = driver

	def on_message_received(self, new_messages):
		for message in new_messages:
			if message.sender.id == contact_A:
				self.driver.forward_messages(contact_B, [message.id])


if __name__ == '__main__':
	run()