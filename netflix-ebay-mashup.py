import json
import requests
import unittest


class Shows():
	def __init__(self, filmstar_name, release_year, shows_all):
		self.filmstar_name = filmstar_name
		self.release_year = release_year
		self.shows_all = shows_all
		self.shows_selected = []

	def __str__(self):
		return "\nThis instance represents the shows of filmstar " + self.filmstar_name + " for the release year " + str(self.release_year) + ". There were totally " + str(len(self.shows_all)) + " shows released that year for this filmstar."

	def sort_shows(self):
		try:
			self.shows_all = sorted(self.shows_all, key = lambda d : float(d["rating"]), reverse = True)
		except Exception, e:
			print "Shows: sort_shows(): " + str(e)

	def select_shows(self):
		try:
			for show_dct in self.shows_all:
				self.display_shows(show_dct)
				keypress = raw_input("\nPress 's' to select this show (press any other key to skip): ")
				if keypress.lower() == 's':
					self.shows_selected.append(show_dct)
					print "\nThe show with ID " + str(show_dct["show_id"]) + " has been added to your list of selected shows."
				else:
					print "\nThe show with ID " + str(show_dct["show_id"]) + " has been skipped."
			if len(self.shows_selected) > 0:
				return True
			else:
				return False
		except Exception, e:
			print "Shows: select_shows(): " + str(e)

	def display_shows(self, show_dct):
		try:
			print "\nShow ID: " + str(show_dct["show_id"])
			print "Show Title: " + show_dct["show_title"]
			print "Summary: " + show_dct["summary"]
			print "Release Year: " + show_dct["release_year"]
			print "Runtime: " + show_dct["runtime"]
			print "Rating: " + show_dct["rating"]
			print "Category: " + show_dct["category"]
			print "Cast: " + show_dct["show_cast"]
			print "Director: " + show_dct["director"]
			print "Poster Link: " + show_dct["poster"]
		except Exception, e:
			print "Shows: display_shows(): " + str(e)


class EbayItems():
	def __init__(self, show_selected, max_price, top_rated = True, max_items = 10):
		self.show_selected = show_selected
		self.max_price = max_price
		self.top_rated = top_rated
		self.max_items = max_items
		self.ebay_items = []

	def __str__(self):
		return "\nThis instance represents a set of items for the selected show with the filters max_price = " + str(self.max_price) + ", top_rated = " + str(self.top_rated) + " and max_items = " + str(self.max_items)

	def fetch_items(self):
		base_url = "http://svcs.ebay.com/services/search/FindingService/v1"
		application_token = "OmkarSun-SI506Pro-PRD-945f0c74d-5d0a28f1"
		url_params = { 'SECURITY-APPNAME' : application_token, 'OPERATION-NAME' : "findItemsByKeywords", 'SERVICE-VERSION' : "1.0.0", 'RESPONSE-DATA-FORMAT' : "JSON", 'keywords' : self.show_selected["show_title"], 'paginationInput.entriesPerPage' : self.max_items, 'GLOBAL-ID' : "EBAY-US", 'siteid' : 0 }
		try:
			r = requests.get(base_url, url_params)
			response = json.loads(r.text[32:-2])
			filtered_response = filter(lambda x : str(x["primaryCategory"][0]["categoryName"][0]) == "DVDs & Blu-ray Discs" and str(x["topRatedListing"][0]).lower() == str(self.top_rated).lower() and float(x["sellingStatus"][0]["currentPrice"][0]["__value__"]) <= self.max_price, response["searchResult"][0]["item"])
			file_handle = open("cache-ebay.txt", 'w')
			for each_item in filtered_response:
				file_handle.write(json.dumps(each_item) + "\n")
			file_handle.close()
		except Exception, e:
			print "EbayItems: fetch_items(): " + str(e)

	def read_cache(self):
		try:
			file_handle = open("cache-ebay.txt", 'r')
			self.ebay_items = [json.loads(each_item) for each_item in file_handle]
			file_handle.close()
		except Exception, e:
			print "EbayItems: read_cache(): " + str(e)

	def display_items(self):
		try:
			if len(self.ebay_items) > 0:
				print "\nSorting the items from highest to lowest price ..."
				self.ebay_items = sorted(self.ebay_items, key = lambda x : float(x["sellingStatus"][0]["currentPrice"][0]["__value__"]), reverse = True)
				print "\nDisplaying the details of each item below ..."
				count_items = 0
				for each_item in self.ebay_items:
					count_items += 1
					print "\nRetrieval No: " + str(count_items)
					if "itemId" in each_item.keys():
						print "Item ID: " + each_item["itemId"][0]
					if "title" in each_item.keys():
						print "Title: " + each_item["title"][0]
					if "viewItemURL" in each_item.keys():
						print "Item URL: " + each_item["viewItemURL"][0]
					if "galleryURL" in each_item.keys():
						print "Item Image: " + each_item["galleryURL"][0]
					if "condition" in each_item.keys():
						if "conditionDisplayName" in each_item["condition"][0].keys():
							print "Item Condition: " + each_item["condition"][0]["conditionDisplayName"][0]
					if "primaryCategory" in each_item.keys():
						if "categoryName" in each_item["primaryCategory"][0].keys():
							print "Category: " + each_item["primaryCategory"][0]["categoryName"][0]
					if "sellingStatus" in each_item.keys():
						if "currentPrice" in each_item["sellingStatus"][0].keys():
							print "Current Price: " + each_item["sellingStatus"][0]["currentPrice"][0]["@currencyId"] + " " + each_item["sellingStatus"][0]["currentPrice"][0]["__value__"]
					if "sellingStatus" in each_item.keys():
						if "sellingState" in each_item["sellingStatus"][0].keys():
							print "Selling State: " + each_item["sellingStatus"][0]["sellingState"][0]
					if "shippingInfo" in each_item.keys():
						if "shippingType" in each_item["shippingInfo"][0].keys():
							print "Shipping Type: " + each_item["shippingInfo"][0]["shippingType"][0]
						if "shippingServiceCost" in each_item["shippingInfo"][0].keys():
							print "Shipping Cost: " + each_item["shippingInfo"][0]["shippingServiceCost"][0]["@currencyId"] + " " + each_item["shippingInfo"][0]["shippingServiceCost"][0]["__value__"]
						if "shipToLocations" in each_item["shippingInfo"][0].keys():
							print "Shipping Coverage: " + each_item["shippingInfo"][0]["shipToLocations"][0]
					if "returnsAccepted" in each_item.keys():
						print "Returns Accepted: " + each_item["returnsAccepted"][0].capitalize()
			else:
				print "\nNo items were available for your search criteria!"
		except Exception, e:
			print "EbayItems: display_items(): " + str(e)


def fetch_shows_from_cache(filmstar_name, release_year):
	try:
		file_handle = open("cache-netflix.txt", 'r')
		shows_dct = [json.loads(record_str) for record_str in file_handle]
		shows_all = [record_dct for record_dct in shows_dct if "Dwayne Johnson" in record_dct['show_cast'] and record_dct['release_year'] == str(release_year)]
		file_handle.close()
		return shows_all
	except Exception, e:
		print "fetch_shows_from_cache(): " + str(e)
	return []


def main():
	filmstar_name = ""
	while filmstar_name == "":
		filmstar_name = raw_input("Please enter the name of the filmstar: ")
		filmstar_name.strip()

	release_year = ""
	while release_year == "":
		try:
			release_year = int(raw_input("Please enter the release year to search (YYYY): "))
		except Exception, e:
			print "main(): " + str(e)

	shows_all = fetch_shows_from_cache(filmstar_name, release_year)
	if len(shows_all) > 0:
		shows_inst = Shows(filmstar_name, release_year, shows_all)
		print shows_inst
		shows_inst.sort_shows()
		shows_selected_status = shows_inst.select_shows()
		if shows_selected_status == False:
			print "\nYou selected no shows to search for on Ebay. Thank you for using the program."
		else:
			print "\nWe will now search for items related to the selected shows on Ebay..."
			for show_selected in shows_inst.shows_selected:
				print "\nConsider the show with the title: " + show_selected["show_title"]
				max_price = ""
				while max_price == "":
					try:
						max_price = float(raw_input("\nPlease enter the maximum amount ($) you are willing to pay: "))
					except Exception, e:
						print "main(): " + str(e)

				top_rated = ""
				while type(top_rated) != bool:
					try:
						top_rated = raw_input("\nPlease enter whether you want to search for top rated listings (Y/N): ")
						if top_rated.lower() == 'y':
							top_rated = True
						elif top_rated.lower() == 'n':
							top_rated = False
					except Exception, e:
						print "main(): " + str(e)

				max_items = 0
				while max_items <= 0 or max_items > 1000:
					try:
						max_items = int(raw_input("\nPlease enter the maximum number of entries to search (<=1000): ")) 
					except Exception, e:
						print "main(): " + str(e)

				ebay_inst = EbayItems(show_selected, max_price, top_rated, max_items)
				print ebay_inst
				ebay_inst.fetch_items()
				ebay_inst.read_cache()
				ebay_inst.display_items()
	else:
		print "There were no shows featuring " + filmstar_name + " for the year " + str(release_year) + "."

main()


############################## UNIT TESTS ARE WRITTEN BELOW THIS LINE ##############################
example1 = Shows("Dwayne Johnson", 2008, [])
example2 = EbayItems({}, 100, True, 500)
example3 = Shows("Colin Firth", 1996, [])
example4 = EbayItems({}, 35, False, 200)

class ProjectUnitTest(unittest.TestCase):
	def test_1(self):
		self.assertEqual(len(fetch_shows_from_cache("Dwayne Johnson", 2013)), 4, "Data in the cache is not correct! There should be 4 shows of Dwayne Johnson for the year 2013.")

	def test_2(self):
		self.assertEqual(len(fetch_shows_from_cache("Tom Cruise", 1957)), 0, "Data in the cache is not correct! There are no shows of Tom Cruise for the year 1957.")

	def test_3(self):
		self.assertTrue(isinstance(example1, Shows), "The instance is not of the class Shows!")

	def test_4(self):
		self.assertTrue(isinstance(example2, EbayItems), "The instance is not of the class EbayItems!")

	def test_5(self):
		self.assertFalse(isinstance(example3, EbayItems), "The instance is of the class EbayItems!")

	def test_6(self):
		self.assertFalse(isinstance(example4, Shows), "The instance is of the class Shows!")

	def test_7(self):
		self.assertEqual(example1.filmstar_name, "Dwayne Johnson", "The value of filmstar_name variable should be Dwayne Johnson!")

	def test_8(self):
		self.assertEqual(example2.max_price, 100, "The value of the max_price variable should be 100!")

	def test_9(self):
		self.assertEqual(example2.top_rated, True, "The value of top_rated variable should be Boolean True!")

	def test_10(self):
		self.assertEqual(example3.release_year, 1996, "The value of release_year variable should be 1996!")

	def test_11(self):
		self.assertEqual(example4.max_items, 200, "The vaue of the max_items variable should be 200!")

	def test_12(self):
		self.assertEqual(type(example1), type(example4), "Both the parameters must be instances of any class!")

unittest.main(verbosity=2)

