from django.shortcuts import render
from .forms import searchForm,indexdataForm
from django.forms.models import model_to_dict
from .models import Document,query
import hashedindex

# Create your views here.
def index(request):
    submitbutton = request.POST.get("submit")
    data=vars(Document.objects.values('doc'))

    list_result =data
    print(list_result)
    form=indexdataForm(request.POST or None)
    if form.is_valid():
        datum=form.cleaned_data.get('Document')
    context={"form":form,"data":list_result}
    return render(request,"search/index.html",context)
    #return datum



def search(request):
    submitbutton = request.POST.get("submit")
    s_query = request.POST.get("q")
    
    form = searchForm(request.POST or None)
    if form.is_valid():
        #form.save()
        s_query = form.cleaned_data.get('query')
    query=request.POST.get('q')
    print(query)
    #code=index(request)
    
    indexer = hashedindex.HashedIndex()
    string_ip = """So since the train was Late. It was stopped in Erode and Held there for an Hour from 4 to 5 AM. We were to reach Bangalore by 8 in the Morning but yet here we are 200 Km from Bangalore. But yet it had its perks. I saw the Eastern Ghats for the First time. The Villages the train Passed in Tamil Nadu. Not eating Breakfast till Noon etc… So anyways we reached Bangalore by 11 AM in the Morning. We were planning to go First to Christ University Campus since Red Hat’s DevConf was being held. It was also an Oppurtunity to meet some fellow Campus Experts. So we got on a Bus from KSR to Christ University Campus. But due to our misinformation that bus was to Another Christ University Campus away from the City. Damn There were 3 Christ Campuses in bangalore Itself. So we got off somewhere and took a Cab to the venue of ETHIndia. We reached the Venue of ETHIndia by 12PM. We found one of our frined Sreeram there Vlogging with his Gimbal Camera.\n\n The Food was free and that was so delicious. It was a new cuisine which I had never tasted before. So we ate our Breakfast/Lunch and went to a conference hall. We got in when the guys from Lendroid were talking about their platform. Time passed and I found these things talks quite Boring. I got out of the room and met Anoop who goes by Kai as his handle. He was also from Kerala. Then Subin and Varun came. Then I met Allen and his team mate Ushana. In the evening Sreeram was interviewing Eylon from Do Stack and I met him and we listened to his story on how he got into Blockchain and stuff. Then there was a talk from Vitalik, the founder of Ethereum.
\n\n The hackathon actually started in the Evening by 7 PM. All of us were given a Bag with 2 Notebooks, Some Stickers and 4 Tshirts. Then I met Syamettan from Mozilla Kerala.He was the maintainer of Keralarescue.in . He was there for some venue arrangements. Then I also met two volunteers for the Hackathon who were friends of Syamettan. We started hacking on something dealing with IPFS and Decentralization. I made the frontend for the stuff. Time passed by. Then I actually met the person sitting infront of me who was also a Malayali. I was thrilled when I heard he was from Pala, Kottayam. At least someone who understands my slang(Kottayam’s Malayalam is the best form of malayalam. The other guys were not from Kottayam though, so it was hard for them to understand some words I was saying). A midnight we went just for a walk with Syamettan. We wanted a coffee but no shops were open. we came back. Oh I didnt tell you about the unlimited supply of Monster Energy Drink Right? Yep unlimited."""
    # To Lower and Indexing Function
    def replacer(s):
        s = s.replace(".", "")  # removed periods
        s = s.replace(",", "")  # removed commas
        s = s.replace("[", "")
        s = s.replace("]", "")
        s = s.replace("(", "")
        s = s.replace(")", "")
        s=s.replace("'","")
        return s
    def toLower(s):
        s=replacer(s)
        string_low = s.lower()  # convert to lowercase
        spl = string_low.split("\n\n")  # split with para
        uid_list = []
        for i in range(len(spl)):
            uid_list.append(i+1)
        return spl, len(spl), uid_list


    st_arr, length, uid = toLower(string_ip)

    # Converting List to String
    def toString(s):
        str = " "
        return str.join(s)


    sparr = toString(st_arr)
    sparr_split = sparr.split(" ")


    for i in range(length):
        for j in range(len(sparr_split)):
            indexer.add_term_occurrence(sparr_split[j], uid[i])


    def doc_splitter(query):
        for j in range(len(uid)):
            for i in range(len(st_arr)):
                sparr = toString(st_arr[i])
                sparr_split = sparr.split(" ")
                indexer.add_term_occurrence(sparr_split[i], uid[j])
        indexes=indexer.items()
        if query in indexes:
            print(indexes.get(query))
            return indexes.get(query)

    index_fin=doc_splitter(query)
    context = {"form": form,"index":index_fin}
    return render(request, "search/search.html", context)
