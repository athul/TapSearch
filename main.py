import hashedindex
index=hashedindex.HashedIndex()
string_ip='''This was the First Day in the 2nd Year of College. I had the train to Bangalore in the evening of the Day. So I had to get all the prior permissions from our Tutuor and our HOD. Phew, our tutor made me run to our department to another part of the Campus twice. Atleast than run made everything smoother for me. So I headed Home and Packed up for my trip and borrowed the Laptop from my cousin. Thanks to my Uncle who gave me 3 Big Books for my Cousin in Bangalore for His Studies. Damn They were Heavy. So I went to the Railway Station and got on a Train to Ernakulam South where the Train to Bangalore is to be departed. This was my rendezvous point with Devdutt Shenoi. So our train was at 8.35Pm but it was late by Half-an-Hour. The Train Came at 9.15 PM. We got on, my Seat was 2 Bogeys from Devdutt but in the beggining we ate pizza together. 3rd Time I was eating Pizza in 19 Years. Some people got from thrissur and I chatted with them for some time. Went to Sleep.\n\n So since the train was Late. It was stopped in Erode and Held there for an Hour from 4 to 5 AM. We were to reach Bangalore by 8 in the Morning but yet here we are 200 Km from Bangalore. But yet it had its perks. I saw the Eastern Ghats for the First time. The Villages the train Passed in Tamil Nadu. Not eating Breakfast till Noon etc… So anyways we reached Bangalore by 11 AM in the Morning. We were planning to go First to Christ University Campus since Red Hat’s DevConf was being held. It was also an Oppurtunity to meet some fellow Campus Experts. So we got on a Bus from KSR to Christ University Campus. But due to our misinformation that bus was to Another Christ University Campus away from the City. Damn There were 3 Christ Campuses in bangalore Itself. So we got off somewhere and took a Cab to the venue of ETHIndia. We reached the Venue of ETHIndia by 12PM. We found one of our frined Sreeram there Vlogging with his Gimbal Camera. The Food was free and that was so delicious. It was a new cuisine which I had never tasted before. So we ate our Breakfast/Lunch and went to a conference hall. We got in when the guys from Lendroid were talking about their platform. Time passed and I found these things talks quite Boring. I got out of the room and met Anoop who goes by Kai as his handle. He was also from Kerala. Then Subin and Varun came. Then I met Allen and his team mate Ushana. In the evening Sreeram was interviewing Eylon from Do Stack and I met him and we listened to his story on how he got into Blockchain and stuff. Then there was a talk from Vitalik, the founder of Ethereum.'''
# To Lower and Indexing Function
def toLower(s):
    s=s.replace(".,[]()1234567890","")# removed periods
    """ s=s.replace(",","")# removed commas
    s=s.replace("[","")
    s=s.replace("]","")
    s=s.replace("(","")
    s=s.replace(")","") """
    string_low=s.lower()# convert to lowercase
    spl=string_low.split('\n\n')# split with para
    uid_list=[]
    for i in range(len(spl)):
        uid_list.append(id(spl[i]))
    return spl,len(spl),uid_list
st_arr,length,uid=toLower(string_ip)
print(length,uid)

# Converting List to String 
def toString(s):
    str=" "
    return str.join(s)
sparr=toString(st_arr)
sparr_split=sparr.split(" ")
#print(sparr.split(" "))
for i in range(length):
    for j in range(len(sparr_split)):
        index.add_term_occurrence(sparr_split[j],uid[i])
def doc_splitter():
    for j in range(len(uid)):
        for i in range(len(st_arr)):
            sparr=toString(st_arr[i])
            sparr_split=sparr.split(" ")
            index.add_term_occurrence(sparr_split[i],uid[j])
    print(index.items())
doc_splitter()