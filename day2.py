from collections import Counter
import itertools

box_ids = ["rvefnvyxzbodgpnpkumawhijsc",
           "rvefqtyxzsddglnppumawhijsc",
           "rvefqtywzbodglnkkubawhijsc",
           "rvefqpyxzbozglnpkumawhiqsc",
           "rvefqtyxzbotgenpkuyawhijsc",
           "rvefqtyxzbodglnlkumtphijsc",
           "rwefqtykzbodglnpkumawhijss",
           "rvynqtyxzbodglnpkumawrijsc",
           "rvefqtyxlbodgcnpkumawhijec",
           "rvefqtyxzbodmlnpnumawhijsx",
           "rvefqtyxzbqdbdnpkumawhijsc",
           "rvefqtyxzlodblnpkuiawhijsc",
           "rvefqtyizrodelnpkumawhijsc",
           "rveffjyxzgodglnpkumawhijsc",
           "rvefqjyxzbodalnpkumadhijsc",
           "rvefqtidzbodglnpkumawhdjsc",
           "hvefqtygzbodglnpkumawhijfc",
           "rzefqtyxzbodglfhkumawhijsc",
           "rmefqtyxzbolglnpkumaehijsc",
           "rnefqqyxzbodglnhkumawhijsc",
           "rvwfqvyxzbodglnpcumawhijsc",
           "rvefqtyxzbokgltpkumavhijsc",
           "rvefciyxzbodglnmkumawhijsc",
           "rvefptyxzbodglnpkuhashijsc",
           "rvefqtyxzrodglnpkxmawhiqsc",
           "rvefqtyxzbotglnpkumawriwsc",
           "rvufqtyxzbodglnplumawhijvc",
           "rvefutykzbodglnpkumaahijsc",
           "rvefqtyxqbodgllprumawhijsc",
           "rvegqttxzbodgllpkumawhijsc",
           "dvefqtyxzsodglnpkumawdijsc",
           "rvefqtyxkbodglnfkumawhijsj",
           "rvefqtyxzbodnlnpcumawhijnc",
           "rvefqtyxzbodglfpkuocwhijsc",
           "rvecqtyxzbbdganpkumawhijsc",
           "rvefytyxzbodglnpkubgwhijsc",
           "rvefxtyazbomglnpkumawhijsc",
           "rvefqgyxzbodglnpkumawyiksc",
           "avefqtyxzbodglnfkummwhijsc",
           "fvefqtyxzbbdglnpkumswhijsc",
           "rvefqtyxzxodglnpkumuuhijsc",
           "rvezqtyxzbydclnpkumawhijsc",
           "rvefqtyxzbohglnpkumawdijjc",
           "rvejqtyxzbodrlnpkumawhijsd",
           "rvefitzxzbxdglnpkumawhijsc",
           "rvefutyxzbvdglnikumawhijsc",
           "rvefqtyazbodgqnbkumawhijsc",
           "rvefqtyxzbolglnpkwmajhijsc",
           "rvefqtyxzjodglnpgwmawhijsc",
           "rvefhtyxzbodglbpaumawhijsc",
           "mvexqtyxzbodglnpkumawrijsc",
           "rvefqtyxwbodglnpkumawhbxsc",
           "rvefqtyxzbodgsnpkudawsijsc",
           "rvwfqtyxzbonglnwkumawhijsc",
           "rvefqtyxzjodglnpkfmawhwjsc",
           "rvefqtyxzbodglntkumughijsc",
           "rvefctyxzbodglnpkumawhiwsx",
           "avefqtyvzbodglnpkumawhijsb",
           "rfefqtyxzlodglnphumawhijsc",
           "rvefqtyxzfowglnpkumaehijsc",
           "rvhfvtyxzbodgqnpkumawhijsc",
           "rfefqtyxzbodglapkumuwhijsc",
           "rvefqclxzbodglnzkumawhijsc",
           "qvefqtyxzbodglnckumcwhijsc",
           "rvefqtyxzkodglnpkymawgijsc",
           "rvefqtyxzbodgfnpkumafhizsc",
           "rvefqtyxzbodglnxkumavhijsf",
           "rvevqtyxzbodgpnpkurawhijsc",
           "rvefqtyxziodglnpkubawhijss",
           "rrefqtpxzyodglnpkumawhijsc",
           "rvefqfyxzbodglcpkxmawhijsc",
           "rvefdtyxzbodglnpkumvwhijsn",
           "rverqtyxzbodglnpkwmawhijuc",
           "rvecjtyxzboxglnpkumawhijsc",
           "rvefqtyxzbodglnpkqmaxhifsc",
           "rtnfqtyxzbodglnpkumawhijmc",
           "lvefqtyxzbodelnpkumawhijsz",
           "dvefqtyxzbbdgvnpkumawhijsc",
           "rvefqlyhzbodglnpkumtwhijsc",
           "roefqtyxlbodglnpkumawhyjsc",
           "rvefqsydzjodglnpkumawhijsc",
           "rveybtyxzbodglnpkumawhijsn",
           "rvefqtyhzbodgvnpmumawhijsc",
           "rvefqxyazboddlnpkumawhijsc",
           "vvefqtyxzbohglqpkumawhijsc",
           "reefhtyxzbodglnpkkmawhijsc",
           "rvefqtyxzbodglnpkulowhijrc",
           "rveqqtyxzbodgknpkumawhijsk",
           "jvefqtqxzbodglnpkumawiijsc",
           "rvefqtyxzboxglnpvuqawhijsc",
           "rvefquyxzbodglwwkumawhijsc",
           "rvefqtyxzbodnlnpkumawhgjbc",
           "rvdfqthxdbodglnpkumawhijsc",
           "rvefqtyxzbodllnpkumawhujsb",
           "evefqtyxzboyglnpkumowhijsc",
           "rvefktyxzbomglnpzumawhijsc",
           "rvefqtyxzbodhlnnkrmawhijsc",
           "rvefqtyxrbodglnpkujaehijsc",
           "rvefqtyzzbodglnpkumrwhijsb",
           "evefqtyxzpodglfpkumawhijsc",
           "rvefqtyxibodglkpyumawhijsc",
           "rrefqtyxzbodglnpkudawhajsc",
           "rvifqtyxzbodglxpkumawhijlc",
           "rxefqtyxzbedglnpkumawhijsp",
           "rvnfqtyxzbopglnpkuqawhijsc",
           "rvefqtyxkbodglnpoumawoijsc",
           "dvefwtyxzbodglnpksmawhijsc",
           "rvkfqtyxzbodglnpkdmawhijsa",
           "rcefytyxzzodglnpkumawhijsc",
           "rvefqtkxzbodglnpktqawhijsc",
           "nvezqhyxzbodglnpkumawhijsc",
           "rrefqtyxzbodgunpkumpwhijsc",
           "rvefqtaxzbodgknpkumawhijic",
           "pvefqtyxzbodglnpkuxawsijsc",
           "rvefqtyxzbodglkpvumawhjjsc",
           "wvefqtyxzkodglnpkumawhhjsc",
           "rzefqtyxzbotglnpkumawhxjsc",
           "rvefqtxpzbodglnpkumawzijsc",
           "bgefqtyxzbodglnpkrmawhijsc",
           "rvefqlyxzbodglnpkumilhijsc",
           "cbefqtyxzbodglnpkumawhiesc",
           "rvefqtyxzbydelnpkumahhijsc",
           "rvefntyxzbodglnpkumaehijsw",
           "rverqtyxztodglopkumawhijsc",
           "rvefqtyxzdodgwrpkumawhijsc",
           "rvefqtyxibodglnikumawhtjsc",
           "qvafqtyxzbodglnpkurawhijsc",
           "rvefqtyxwbodglnpaumawoijsc",
           "rvefqtyxzoodglndknmawhijsc",
           "rvdfqtlxzyodglnpkumawhijsc",
           "rvefqtyxzbodglngfumawhinsc",
           "rsefqtyxzbodglnpkumawhijek",
           "rvoestyxzbodglnpkumawhijsc",
           "svefqtyxzboaglnprumawhijsc",
           "rvefqtybzbodgwnpkumawwijsc",
           "rvefqtyxzdwdglnpkvmawhijsc",
           "rvlfqtyxzbodglnpkrmawhixsc",
           "rvefqtyxwbodglepkumawhijsd",
           "rvefqtbxzbodglnqkumawhijmc",
           "rvefqtzxzbodglnpkumuzhijsc",
           "rvefqtyxzbodglnpkumawzwnsc",
           "rvwfqtyxzboiglnpkumawhijsg",
           "rtehotyxzbodglnpkudawhijsc",
           "rvegqtyxzbodglnpyumawhijsl",
           "rvecqtyxzbsdglnpkumawhojsc",
           "rvefqtyxzbodmlnpkumaghijfc",
           "rvefqtyxzxodglnpkumanvijsc",
           "rvefqtyxzbodglnbiugawhijsc",
           "lvefqtlxzbodglnplumawhijsc",
           "rvefqtyxvbodglnpkumaldijsc",
           "rmefqtyxzbodgvnpkuuawhijsc",
           "rvefqtyxzbodglnpkymeuhijsc",
           "rvefqtyxzuodganpsumawhijsc",
           "rxefqtyxzbodglnpkumgwhijwc",
           "rvefgtyxzbodglnpkudawxijsc",
           "ahefqtyxzbodglnpkumawhejsc",
           "rfefqtyxzbzdglnpkusawhijsc",
           "rvefqtyszqodgljpkumawhijsc",
           "rvefqtylzboiglnpkumrwhijsc",
           "rvefqtyxzltdglnpkumawhijsu",
           "rbefqtyxzbodglnpqumawhijsi",
           "rvefqtyozpodglnpkumawhijsa",
           "zvefqtyxzpopglnpkumawhijsc",
           "rvefqtyxzbodglnfkqmawhijsp",
           "rvefqtyxzbodgliakumawhijsf",
           "rvefqtymzrodgfnpkumawhijsc",
           "ivejqtyxzbodglnpkumawhijuc",
           "rvefqtyxzbodflnpkxwawhijsc",
           "dvrfqtyxzbodglnpkumashijsc",
           "rqefqtyxzbwdglnpkumawvijsc",
           "tvefqtkxzbodgltpkumawhijsc",
           "rvefdtyxzbodguxpkumawhijsc",
           "rveqqtyxvbodglnykumawhijsc",
           "rvefqtypzcovglnpkumawhijsc",
           "rvefqnyxzbosglnpkumdwhijsc",
           "rvefstjxzbodslnpkumawhijsc",
           "rvefqzyxzpodglnpkummwhijsc",
           "rvefqkyxzbodglnhgumawhijsc",
           "rvufqvyxzbodklnpkumawhijsc",
           "rvefotyxzhodglnpkumawhijsk",
           "rvefqtyxzbokglnpkumawvcjsc",
           "lvefqtyxzbolglnpkumawoijsc",
           "rvefqtywzoodglfpkumawhijsc",
           "rvehqtqxzbodglnpkumawhcjsc",
           "rqefqtyxzbodolnpkumjwhijsc",
           "rvefqtyxzbodglrpkunawgijsc",
           "rvefqtyxzbodglamkumawdijsc",
           "rvefvtyzzbodllnpkumawhijsc",
           "rvefqtyxzbldglnpfcmawhijsc",
           "rvefppyxzbodglnpkucawhijsc",
           "rvefquyuzbodglnpkumkwhijsc",
           "rvefqtyxzbodgqxpkumawhivsc",
           "rtefotyxzbodglnpkudawhijsc",
           "rvefqtyxzbodgbnmkuzawhijsc",
           "ivefqtyxzbodgsnpkumzwhijsc",
           "rvhfqtyxzbodolnpkumawhijsz",
           "rvefvtyxzbodwlnpkusawhijsc",
           "riemqtyxzbodglnpkumawhiasc",
           "rvtfqtyxzbqdglnpkumawuijsc",
           "raesqtyxzbodglnpkumawhijsj",
           "rvefqtyxzbodalmpkumawhihsc",
           "rvefqtlxzbodgznpkkmawhijsc",
           "rvefqbyxzbodglgpkubawhijsc",
           "rvefqtyxnbodgxnpkumswhijsc",
           "rvefqtyxzkodvlnukumawhijsc",
           "rvefqtyzzbocglnpkumafhijsc",
           "rvhfqtyxzbodglmpkumgwhijsc",
           "rvsfrtyxzbodnlnpkumawhijsc",
           "rvefqtyxzbxdglnpkujcwhijsc",
           "rvefqtyvzrodglnphumawhijsc",
           "reetatyxzbodglnpkumawhijsc",
           "rvefqtyxzbodglnpzumaoqijsc",
           "ovefqtyyzbodglnvkumawhijsc",
           "rvefqbyxzbodnlnpkumawhijsi",
           "xvefqtyxzbodgrnpkumawrijsc",
           "rvebqtyxzbodglnpkumazhiasc",
           "rqeretyxzbodglnpkumawhijsc",
           "rvefqtyxzyodglapkumvwhijsc",
           "rvesqxyxzbodglnpvumawhijsc",
           "rvefqtyxeborglnpkufawhijsc",
           "rvecqtyxzbodflnpkumawnijsc",
           "rvefdpyxtbodglnpkumawhijsc",
           "rvefqtyfzbodclnpkymawhijsc",
           "rvefqtywzbodglnpxumawhiusc",
           "rvefqtyxzbodglnpkumawzbjwc",
           "rvewqtyxdbodglnpxumawhijsc",
           "rvefqtyxzgocglnpkgmawhijsc",
           "rvufqtyxzbodggnpkuzawhijsc",
           "rvefqtynzlodgllpkumawhijsc",
           "rvedqtyxzbodghnpkumawhujsc",
           "rvefqtyxlbodgnnpkpmawhijsc",
           "rvefqtyxzboqglnpkzmawhijec",
           "rvefqtyxzbodglnpkfmwwyijsc",
           "rwefqtkxzbodzlnpkumawhijsc",
           "rvefqtyxvbodglnpkufawhyjsc",
           "rvefqtyxzbodgltpkumawhqmsc",
           "rvefctyxzbodglfpkumathijsc",
           "rvefqtyxzbodgfnpkuuawhijfc",
           "rvefqttxzbodglnpmumawhijwc",
           "rvefqtyxzbodglnpkqmawhihsj",
           "rvefqtyxzbsdglcnkumawhijsc",
           "rvbiqtyxzbodglnpkumawhijlc",
           "rnefqtylzvodglnpkumawhijsc",
           "mvefqtyxzbddglnpkumcwhijsc",
           "rvefwtyxzbodglnpkgmawhijxc",
           "rvefqtyxljodglnpkumxwhijsc",
           "rvefqtyxzbodglnpkuprwhijsd",
           "rcxfqtyxzbldglnpkumawhijsc",
           "rvetqtyxzbojglnpkumewhijsc",
           "rvxfqtyxzbtdglnpkbmawhijsc"]

# Part 1
checksum_two_counter, checksum_three_counter = 0, 0

for each_id in box_ids:
    c = Counter(each_id)
    letter_counts = c.values()

    checksum_three_counter += 1 if 3 in letter_counts else 0
    checksum_two_counter += 1 if 2 in letter_counts else 0

print(f"Checksum = {checksum_three_counter * checksum_two_counter}")

# Part 2
for s, t in itertools.combinations(box_ids, 2):  # Get all tuple combinations of box_ids
    difference, position = 0, None
    for i, (first, second) in enumerate(zip(s, t)):  # Go over pairs of letters
        if first != second:
            difference += 1
            position = i  # Overwrite since we want exactly one occurrence
    if difference == 1:
        common_letters = s[:position] + s[position + 1:]
        print(f"Found a match: {common_letters}")
