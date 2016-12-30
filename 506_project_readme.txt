506 Final Project Readme

1. Describe your project in 1-4 sentences. Include the basic summary of what it does, and the output that it should generate/how one can use the output and/or what question the output answers. 

I am creating an “API mashup” that would enable a user to search a local cache (obtained from the Netflix Roulette REST API) for shows about a given filmstar for a particular year and display his/her shows from high to low rating. The program would then allow the user to select the shows of choice (from the listed shows) and retrieve product listings (DVDs & Blu-ray Discs) about that show from the eBay store using the eBay Finding REST API and display the search results to the user based on the following conditions:
1. User enters the maximum price he/she is willing to pay for the item.
2. User is asked whether he/she would like to search for top rated listings.
3. User is asked to enter the maximum number of retrievals to fetch from Ebay.
4. Ebay items are always listed from highest price to lowest price on the screen.

Results are always cached for both APIs..so I have 2 caches in my program — one is a local permanent cache; the other cache is created during runtime.


2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).

(Your program running should depend on cached data, but OK to write a program that would make more sense to run on live data and tell us to e.g. use a sample value in order to run it on cached data.)

Kindly run the program as follows:
1. python 506_project.py
2. Please enter the name of the filmstar: Dwayne Johnson
3. Please enter the release year to search (YYYY): 2013
4. Press ’s’ to select any retrieval obtained from the local permanent cache
5. Please enter the maximum amount ($) you are willing to pay for each item: 50
6. Please enter whether you want to search for top rated listings (Y/N): Y
7. Please enter the maximum number of entries to search (<=1000): 100
8. The program will search on Ebay by “keyword” and display the first 100 top-rated items from the category “DVDs & Blu-ray Discs” ordered from highest to lowest price.
9. The user can use the details to purchase some product online if interested.
10. The program execution will then end.


SAMPLE OUTPUT:
=======================
Omkars-MacBook-Pro:project omkarsunkersett$ python 506_project.py
Please enter the name of the filmstar: Dwayne Johnson
Please enter the release year to search (YYYY): 2013

This instance represents the shows of filmstar Dwayne Johnson for the release year 2013. There were totally 4 shows released that year for this filmstar.

Show ID: 70226287
Show Title: G.I. Joe: Retaliation
Summary: In this action-packed sequel to G.I. Joe: The Rise of Cobra, the elite anti-terrorist team finds itself framed for treason by global mercenary Zartan.
Release Year: 2013
Runtime: 110 min
Rating: 3.5
Category: Action & Adventure
Cast: Dwayne Johnson, Jonathan Pryce, Byung-hun Lee, Elodie Yung, Ray Stevenson, D.J. Cotrona, Adrianne Palicki, Channing Tatum, Ray Park, Luke Bracey
Director: Jon M. Chu
Poster Link: http://netflixroulette.net/api/posters/70226287.jpg

Press 's' to select this show (press any other key to skip): s

The show with ID 70226287 has been added to your list of selected shows.

Show ID: 70290892
Show Title: The History of the WWE
Summary: This 50-year retrospective chronicles the evolution of the WWE from a small, regional promotion into a worldwide phenomenon. With new interviews from several key personalities past and present, get the inside story behind each WWE era.
Release Year: 2013
Runtime: None
Rating: 3.5
Category: Documentaries
Cast: Bruno Sammartino, Hulk Hogan, Bret Hart, Steve Austin, Dwayne Johnson, Triple H, John Cena
Director: 
Poster Link: http://netflixroulette.net/api/posters/70290892.jpg

Press 's' to select this show (press any other key to skip): 

The show with ID 70290892 has been skipped.

Show ID: 80000755
Show Title: WWE: The Best of Raw and Smackdown
Summary: WWE superstars delivered 52 weeks of action on Raw and SmackDown in 2013, all captured in this collection of the most thrilling matches of the year.
Release Year: 2013
Runtime: N/A
Rating: 3.3
Category: Sports & Fitness
Cast: CM Punk, Ryback, Big Show, Alberto Del Rio, Dwayne Johnson, Paul Heyman, Vince McMahon, John Cena, Jack Swagger, Zeb Colter
Director: 
Poster Link: http://netflixroulette.net/api/posters/80000755.jpg

Press 's' to select this show (press any other key to skip): s

The show with ID 80000755 has been added to your list of selected shows.

Show ID: 70259171
Show Title: Pain & Gain
Summary: Michael Bay's comedic action flick tells the true story of Daniel Lugo and Adrian Doorbal, two Miami muscle heads who become major-league criminals.
Release Year: 2013
Runtime: N/A
Rating: 3.1
Category: Action & Adventure
Cast: Mark Wahlberg, Dwayne Johnson, Anthony Mackie, Tony Shalhoub, Ed Harris, Rob Corddry, Bar Paly, Rebel Wilson, Ken Jeong
Director: Michael Bay
Poster Link: http://netflixroulette.net/api/posters/70259171.jpg

Press 's' to select this show (press any other key to skip): 

The show with ID 70259171 has been skipped.

We will now search for items related to the selected shows on Ebay...

Consider the show with the title: G.I. Joe: Retaliation

Please enter the maximum amount ($) you are willing to pay: 100

Please enter whether you want to search for top rated listings (Y/N): Y

Please enter the maximum number of entries to search (<=1000): 1000

This instance represents a set of items for the selected show with the filters max_price = 100.0, top_rated = True and max_items = 1000

Sorting the items from highest to lowest price ...

Displaying the details of each item below ...

Retrieval No: 1
Item ID: 222275238350
Title: G.I. Joe: Retaliation (DVD, 2013)
Item URL: http://www.ebay.com/itm/G-I-Joe-Retaliation-DVD-2013-/222275238350
Item Image: http://thumbs3.ebaystatic.com/m/mtpd9pnQ9T5WYuw1riijlQA/140.jpg
Item Condition: Brand New
Category: DVDs & Blu-ray Discs
Current Price: USD 6.45
Selling State: Active
Shipping Type: Free
Shipping Cost: USD 0.0
Shipping Coverage: US
Returns Accepted: True

Consider the show with the title: WWE: The Best of Raw and Smackdown

Please enter the maximum amount ($) you are willing to pay: 20

Please enter whether you want to search for top rated listings (Y/N): N

Please enter the maximum number of entries to search (<=1000): 10

This instance represents a set of items for the selected show with the filters max_price = 20.0, top_rated = False and max_items = 10

Sorting the items from highest to lowest price ...

Displaying the details of each item below ...

Retrieval No: 1
Item ID: 282242639145
Title: WWE: The Best of Raw and Smackdown 2013 (DVD, 2014, 3-Disc Set)
Item URL: http://www.ebay.com/itm/WWE-Best-Raw-and-Smackdown-2013-DVD-2014-3-Disc-Set-/282242639145
Item Image: http://thumbs2.ebaystatic.com/pict/2822426391454040_1.jpg
Item Condition: Brand New
Category: DVDs & Blu-ray Discs
Current Price: USD 10.98
Selling State: Active
Shipping Type: Free
Shipping Cost: USD 0.0
Shipping Coverage: US
Returns Accepted: False

Retrieval No: 2
Item ID: 252392366030
Title: WWE: Raw and Smackdown - The Best of 2011 (DVD, 2012, 4-Disc Set) BRAND NEW
Item URL: http://www.ebay.com/itm/WWE-Raw-and-Smackdown-Best-2011-DVD-2012-4-Disc-Set-BRAND-NEW-/252392366030
Item Image: http://thumbs3.ebaystatic.com/m/mgeNS-LgBQ5Op0w87ZwTuNg/140.jpg
Item Condition: Brand New
Category: DVDs & Blu-ray Discs
Current Price: USD 9.99
Selling State: Active
Shipping Type: Flat
Shipping Cost: USD 0.99
Shipping Coverage: US
Returns Accepted: True

Retrieval No: 3
Item ID: 262745692203
Title: WWE: The Best of Raw and Smackdown 2013 (DVD, 2014, 3-Disc Set)
Item URL: http://www.ebay.com/itm/WWE-Best-Raw-and-Smackdown-2013-DVD-2014-3-Disc-Set-/262745692203
Item Image: http://thumbs4.ebaystatic.com/m/mua0JsdU24SGtSDpK9XzN-A/140.jpg
Item Condition: Very Good
Category: DVDs & Blu-ray Discs
Current Price: USD 7.99
Selling State: Active
Shipping Type: Free
Shipping Cost: USD 0.0
Shipping Coverage: US
Returns Accepted: True

Retrieval No: 4
Item ID: 112209159357
Title: NEW WWE: The Best of Raw and Smackdown 2013 (DVD, 2014, 3-Disc Set), Sealed
Item URL: http://www.ebay.com/itm/NEW-WWE-Best-Raw-and-Smackdown-2013-DVD-2014-3-Disc-Set-Sealed-/112209159357
Item Image: http://thumbs2.ebaystatic.com/m/mQhcZSqpVtuT1hUZKZMx6Lw/140.jpg
Item Condition: Brand New
Category: DVDs & Blu-ray Discs
Current Price: USD 7.5
Selling State: Active
Shipping Type: Flat
Shipping Cost: USD 3.5
Shipping Coverage: US
Returns Accepted: False

Retrieval No: 5
Item ID: 222339172110
Title: WWE: RAW AND SMACKDOWN - THE BEST OF 2011 [USED BLU-RAY] 
Item URL: http://www.ebay.com/itm/WWE-RAW-AND-SMACKDOWN-BEST-2011-USED-BLU-RAY-/222339172110
Item Image: http://thumbs3.ebaystatic.com/m/mWNuRZO0wXXDhTyHbiGKOmA/140.jpg
Item Condition: Very Good
Category: DVDs & Blu-ray Discs
Current Price: USD 5.99
Selling State: Active
Shipping Type: Calculated
Shipping Coverage: US
Returns Accepted: True

Retrieval No: 6
Item ID: 162311948293
Title: WWE: The Best of Raw and Smackdown 2014 (DVD, 2015, 3-Disc Set)
Item URL: http://www.ebay.com/itm/WWE-Best-Raw-and-Smackdown-2014-DVD-2015-3-Disc-Set-/162311948293
Item Image: http://thumbs2.ebaystatic.com/m/miIkN3httRTBly_fhihnBNA/140.jpg
Item Condition: Like New
Category: DVDs & Blu-ray Discs
Current Price: USD 4.5
Selling State: Active
Shipping Type: Calculated
Shipping Coverage: US
Returns Accepted: False

Retrieval No: 7
Item ID: 252645345562
Title: WWE: Raw and Smackdown - The Best of 2011 (Blu-ray Disc, 2012, 3-Disc Set)
Item URL: http://www.ebay.com/itm/WWE-Raw-and-Smackdown-Best-2011-Blu-ray-Disc-2012-3-Disc-Set-/252645345562
Item Image: http://thumbs3.ebaystatic.com/m/mWNuRZO0wXXDhTyHbiGKOmA/140.jpg
Item Condition: Like New
Category: DVDs & Blu-ray Discs
Current Price: USD 3.99
Selling State: Active
Shipping Type: Calculated
Shipping Coverage: US
Returns Accepted: False

Retrieval No: 8
Item ID: 291963044221
Title: WWE: THE BEST OF RAW AND SMACKDOWN 2012 (DISCS & INSERT ONLY)
Item URL: http://www.ebay.com/itm/WWE-BEST-RAW-AND-SMACKDOWN-2012-DISCS-INSERT-ONLY-/291963044221
Item Image: http://thumbs2.ebaystatic.com/m/mf17IdChFWMiWtOUg0R6lXQ/140.jpg
Item Condition: Very Good
Category: DVDs & Blu-ray Discs
Current Price: USD 1.25
Selling State: Active
Shipping Type: Free
Shipping Cost: USD 0.0
Shipping Coverage: US
Returns Accepted: False

test_1 (__main__.ProjectUnitTest) ... ok
test_10 (__main__.ProjectUnitTest) ... ok
test_11 (__main__.ProjectUnitTest) ... ok
test_12 (__main__.ProjectUnitTest) ... ok
test_2 (__main__.ProjectUnitTest) ... ok
test_3 (__main__.ProjectUnitTest) ... ok
test_4 (__main__.ProjectUnitTest) ... ok
test_5 (__main__.ProjectUnitTest) ... ok
test_6 (__main__.ProjectUnitTest) ... ok
test_7 (__main__.ProjectUnitTest) ... ok
test_8 (__main__.ProjectUnitTest) ... ok
test_9 (__main__.ProjectUnitTest) ... ok

----------------------------------------------------------------------
Ran 12 tests in 1.024s

OK


3. List all the files you are turning in, with a brief description of each one. (At minimum, there should be 1 Python file, 1 file containing cached data, and the README file, but if your project requires others, that is fine as well! Just make sure you have submitted them all.)

506_project.py : This contains the code of the project.
cache-netflix.txt: This contains the “local and permanently” cached results from the Netflix Roulette REST API.
cache-ebay.txt: This contains the results cached at runtime from the Ebay Finding REST API.
retrieve_shows.py: This contains the code to obtain results from the Netflix Roulette REST API and cache them locally and permanently to disk.
506_project_readme.rtf: This contains the “read me” of the project.


4. Any Python packages/modules that must be installed in order to run your project (e.g. requests, or requests_oauthlib, or...):

Modules used are as follows:
json
requests
unittest


5. What API sources did you use? Provide links here and any other description necessary.

I have used the following two REST APIs:

1. REST API Name: Netflix Roulette API 
Documentation: http://netflixroulette.net/api/
Authentication: Not required
Key: Not required
Account: Not required
Parameters: actor

2. REST API Name: eBay Finding API
Documentation: http://developer.ebay.com/Devzone/finding/CallRef/index.html
Authentication: OAuth 2.0
Key: Application token
Account: Require an account with the eBay developers program.
Parameters: security-appname, operation-name, service-version, response-data-format, keywords, paginationInput.entriesPerPage, global-id, siteid


6. Approximate line numbers in Python file to find the following mechanics requirements (this is so we can grade your code!):
- Sorting with a key function: Lines 18 and 93.
- Use of list comprehension OR map OR filter: filter() used in line 73; list comprehension used in lines 84, 137 and 138.
- Class definition beginning 1: Line 6
- Class definition beginning 2: Line 55
- Creating instance of one class: Line 161
- Creating instance of a second class: Line 196
- Calling any method on any class instance (list all approx line numbers where this happens, or line numbers where there is a chunk of code in which a bunch of methods are invoked): sort_shows() on line 163, select_shows() on line 164 (select_shows() calls display_shows() internally on line 25), fetch_items() on line 198, read_cache() on line 199, display_items() on line 200.
- (If applicable) Beginnings of function definitions outside classes: fetch_shows_from_cache() on line 134, and main() on line 146.
- Beginning of code that handles data caching/using cached data: Line 136 for Netflix local cache, and line 74 for Ebay Finding API
- Test cases: Lines 207 to 250

8. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?

I am doing this project because I would like to learn how to use other REST APIs (other than the ones taught in class) and create my own “API mashup” with them. Normally, people know filmstars by their respective names but know very little about their movies. My Python script would allow users to know more about the shows of a particular actor/actress and also provide multimedia shopping options (DVDs & Blu-ray Discs) online based on the user’s selection.

I found it interesting because I have never used the Ebay Finding API before. Using a new API always helps as you get to learn more by using it. :-)

Yes, it did work out the way I wanted it to work. If you find any “irrelevant” retrievals from Ebay, then it is because of some problem with Ebay’s search engine and not my code. My code simply uses the Ebay API to search for items based on a “keyword” search. 


