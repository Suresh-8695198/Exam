import pandas as pd
l1 = [
    "CA001", "CA002", "CA003", "CA004", "CA005", "CA006", "CA007", "CA008", "CA009", "CA010",
    "CA011", "CA012", "CA013", "CA014", "CA015", "CA016", "CA017", "CA018", "CA019", "CA020",
    "CA021", "CA022", "CA023", "CA024", "CA025", "CA026", "CA027", "CA028", "CA029", "CA030",
    "CA031", "CA032", "CA033", "CA034", "CA035", "CA036", "CA037", "CA038", "CA039", "CA040",
    "CA041", "CA042", "CA043", "CA044", "CA045", "CA046", "CA047", "CA048", "CA049", "CA050",
    "CA051", "CA052", "CA053", "CA054", "CA055", "CA056", "CA057", "CA058", "CA059", "CA060",
    "CA061", "CA062", "CA063", "CA064", "CA065", "CA066", "CA067", "CA068", "CA069", "CA070",
    "CA071", "CA072", "CA073", "CA074", "CA075", "CA076", "CA077", "CA078", "CA079", "CA080",
    "CA081", "CA082", "CA083", "CA084", "CA085", "CA086", "CA087", "CA088", "CA089", "CA090",
    "CA091", "CA092", "CA093", "CA094", "CA095", "CA096", "CA097", "CA098", "CA099", "CA100",
    "CA101", "CA102", "CA103", "CA104", "CA105", "CA106", "CA107", "CA108", "CA109", "CA110",
    "CA111", "CA112", "CA113", "CA114", "CA115", "CA116", "CA117", "CA118", "CA119", "CA120",
    "CA121", "CA122", "CA123", "CA124", "CA125", "CA126", "CA127", "CA128", "CA129", "CA130",
    "CA131", "CA132", "CA133", "CA134", "CA135", "CA136", "CA137", "CA138", "CA139", "CA140",
    "CA141", "CA142", "CA143", "CA144", "CA145", "CA146", "CA147", "CA148", "CA149", "CA150",
    "CA151", "CA152", "CA153", "CA154", "CA155", "CA156", "CA157", "CA158", "CA159", "CA160",
    "CA161", "CA162", "CA163", "CA164", "CA165", "CA166", "CA167", "CA168", "CA169", "CA170",
    "CA171", "CA172", "CA173", "CA174", "CA175", "CA176", "CA177", "CA178", "CA179", "CA180",
    "CA181", "CA182", "CA183", "CA184", "CA185", "CA186", "CA187", "CA188", "CA189", "CA190",
    "CA191", "CA192", "CA193", "CA194", "CA195", "CA196", "CA197", "CA198", "CA199", "CA200",
    "CA201", "CA202", "CA203", "CA204", "CA205", "CA206", "CA207", "CA208", "CA209", "CA210",
    "CA211", "CA212", "CA213", "CA214", "CA215", "CA216", "CA217", "CA218", "CA219", "CA220",
    "CA221", "CA222", "CA223", "CA224", "CA225", "CA226", "CA227", "CA228", "CA229", "CA230",
    "CA231", "CA232", "CA233", "CA234", "CA235", "CA236", "CA237", "CA238", "CA239", "CA240",
    "CA241", "CA242", "CA243", "CA244", "CA245", "CA246", "CA247", "CA248", "CA249", "CA250",
    "CA251", "CA252", "CA253", "CA254", "CA255", "CA256", "CA257", "CA258", "CA259", "CA260",
    "CA261", "CA262", "CA263", "CA264", "CA265", "CA266", "CA267", "CA268", "CA269", "CA270",
    "CA271", "CA272", "CA273", "CA274", "CA275", "CA276", "CA277", "CA278", "CA279", "CA280",
    "CA281", "CA282", "CA283", "CA284", "CA285", "CA286", "CA287", "CA288", "CA289", "CA290",
    "CA291", "CA292", "CA293", "CA294", "CA295", "CA296", "CA297", "CA298", "CA299", "CA300",
    "MA001", "MA002", "MA003", "MA004", "MA005", "MA006", "MA007", "MA008", "MA009", "MA010",
    "MA011", "MA012", "MA013", "MA014", "MA015", "MA016", "MA017", "MA018", "MA019", "MA020",
    "MA021", "MA022", "MA023", "MA024", "MA025", "MA026", "MA027", "MA028", "MA029", "MA030",
    "MA031", "MA032", "MA033", "MA034", "MA035", "MA036", "MA037", "MA038", "MA039", "MA040",
    "MA041", "MA042", "MA043", "MA044", "MA045", "MA046", "MA047", "MA048", "MA049", "MA050",
    "MA051", "MA052", "MA053", "MA054", "MA055", "MA056", "MA057", "MA058", "MA059", "MA060",
    "MA061", "MA062", "MA063", "MA064", "MA065", "MA066", "MA067", "MA068", "MA069", "MA070",
    "MA071", "MA072", "MA073", "MA074", "MA075", "MA076", "MA077", "MA078", "MA079", "MA080",
    "MA081", "MA082", "MA083", "MA084", "MA085", "MA086", "MA087", "MA088", "MA089", "MA090",
    "MA091", "MA092", "MA093", "MA094", "MA095", "MA096", "MA097", "MA098", "MA099", "MA100",
    "MA101", "MA102", "MA103", "MA104", "MA105", "MA106", "MA107", "MA108", "MA109", "MA110",
    "MA111", "MA112", "MA113", "MA114", "MA115", "MA116", "MA117", "MA118", "MA119", "MA120",
    "MA121", "MA122", "MA123", "MA124", "MA125", "MA126", "MA127", "MA128", "MA129", "MA130",
    "MA131", "MA132", "MA133", "MA134", "MA135", "MA136", "MA137", "MA138", "MA139", "MA140",
    "MA141", "MA142", "MA143", "MA144", "MA145", "MA146", "MA147", "MA148", "MA149", "MA150",
    "BCOMCA001", "BCOMCA002", "BCOMCA003", "BCOMCA004", "BCOMCA005", "BCOMCA006", "BCOMCA007", "BCOMCA008", "BCOMCA009", "BCOMCA010",
    "BCOMCA011", "BCOMCA012", "BCOMCA013", "BCOMCA014", "BCOMCA015", "BCOMCA016", "BCOMCA017", "BCOMCA018", "BCOMCA019", "BCOMCA020",
    "ENG001", "ENG002", "ENG003", "ENG004", "ENG005", "ENG006", "ENG007", "ENG008", "ENG009", "ENG010",
    "ENG011", "ENG012", "ENG013", "ENG014", "ENG015", "ENG016", "ENG017", "ENG018", "ENG019", "ENG020",
    "ENG021", "ENG022", "ENG023", "ENG024", "ENG025", "ENG026", "ENG027", "ENG028", "ENG029", "ENG030",
    "ENG031", "ENG032", "ENG033", "ENG034", "ENG035", "ENG036", "ENG037", "ENG038", "ENG039", "ENG040",
    "ENG041", "ENG042", "ENG043", "ENG044", "ENG045", "ENG046", "ENG047", "ENG048", "ENG049", "ENG050",
    "ENG051", "ENG052", "ENG053", "ENG054", "ENG055", "ENG056", "ENG057", "ENG058", "ENG059", "ENG060",
    "ENG061", "ENG062", "ENG063", "ENG064", "ENG065", "ENG066", "ENG067", "ENG068", "ENG069", "ENG070",
    "ENG071", "ENG072", "ENG073", "ENG074", "ENG075", "ENG076", "ENG077", "ENG078", "ENG079", "ENG080",
    "PH001", "PH002", "PH003", "PH004", "PH005", "PH006", "PH007", "PH008", "PH009", "PH010",
    "PH011", "PH012", "PH013", "PH014", "PH015", "PH016", "PH017", "PH018", "PH019", "PH020",
    "PH021", "PH022", "PH023", "PH024", "PH025", "PH026", "PH027", "PH028", "PH029", "PH030",
    "PH031", "PH032", "PH033", "PH034", "PH035", "PH036", "PH037", "PH038", "PH039", "PH040",
    "PH041", "PH042", "PH043", "PH044", "PH045", "PH046", "PH047", "PH048", "PH049", "PH050",
    "PH051", "PH052", "PH053", "PH054", "PH055", "PH056", "PH057", "PH058", "PH059", "PH060",
    "PH061", "PH062", "PH063", "PH064", "PH065", "PH066", "PH067", "PH068", "PH069", "PH070"

]
    
l2=["CS001", "CS002", "CS003", "CS004", "CS005", "CS006", "CS007", "CS008", "CS009", "CS010",
    "CS011", "CS012", "CS013", "CS014", "CS015", "CS016", "CS017", "CS018", "CS019", "CS020",
    "CS021", "CS022", "CS023", "CS024", "CS025", "CS026", "CS027", "CS028", "CS029", "CS030",
    "CS031", "CS032", "CS033", "CS034", "CS035", "CS036", "CS037", "CS038", "CS039", "CS040",
    "CS041", "CS042", "CS043", "CS044", "CS045", "CS046", "CS047", "CS048", "CS049", "CS050",
    "CS051", "CS052", "CS053", "CS054", "CS055", "CS056", "CS057", "CS058", "CS059", "CS060",
    "CS061", "CS062", "CS063", "CS064", "CS065", "CS066", "CS067", "CS068", "CS069", "CS070",
    "CS071", "CS072", "CS073", "CS074", "CS075", "CS076", "CS077", "CS078", "CS079", "CS080",
    "CS081", "CS082", "CS083", "CS084", "CS085", "CS086", "CS087", "CS088", "CS089", "CS090",
    "CS091", "CS092", "CS093", "CS094", "CS095", "CS096", "CS097", "CS098", "CS099", "CS100",
    "CS101", "CS102", "CS103", "CS104", "CS105", "CS106", "CS107", "CS108", "CS109", "CS110",
    "CS111", "CS112", "CS113", "CS114", "CS115", "CS116", "CS117", "CS118", "CS119", "CS120",
    "CS121", "CS122", "CS123", "CS124", "CS125", "CS126", "CS127", "CS128", "CS129", "CS130",
    "CS131", "CS132", "CS133", "CS134", "CS135", "CS136", "CS137", "CS138", "CS139", "CS140",
    "CS141", "CS142", "CS143", "CS144", "CS145", "CS146", "CS147", "CS148", "CS149", "CS150",
    "CS151", "CS152", "CS153", "CS154", "CS155", "CS156", "CS157", "CS158", "CS159", "CS160",
    "CS161", "CS162", "CS163", "CS164", "CS165", "CS166", "CS167", "CS168", "CS169", "CS170",
    "CS171", "CS172", "CS173", "CS174", "CS175", "CS176", "CS177", "CS178", "CS179", "CS180",
    "CS181", "CS182", "CS183", "CS184", "CS185", "CS186", "CS187", "CS188", "CS189", "CS190",
    "CS191", "CS192", "CS193", "CS194", "CS195", "CS196", "CS197", "CS198", "CS199", "CS200",
     "BCOM001", "BCOM002", "BCOM003", "BCOM004", "BCOM005", "BCOM006", "BCOM007", "BCOM008", "BCOM009", "BCOM010",
    "BCOM011", "BCOM012", "BCOM013", "BCOM014", "BCOM015", "BCOM016", "BCOM017", "BCOM018", "BCOM019", "BCOM020",
    "BCOM021", "BCOM022", "BCOM023", "BCOM024", "BCOM025", "BCOM026", "BCOM027", "BCOM028", "BCOM029", "BCOM030",
    "BCOM031", "BCOM032", "BCOM033", "BCOM034", "BCOM035", "BCOM036", "BCOM037", "BCOM038", "BCOM039", "BCOM040",
    "BCOM041", "BCOM042", "BCOM043", "BCOM044", "BCOM045", "BCOM046", "BCOM047", "BCOM048", "BCOM049", "BCOM050",
    "BCOM051", "BCOM052", "BCOM053", "BCOM054", "BCOM055", "BCOM056", "BCOM057", "BCOM058", "BCOM059", "BCOM060",
    "BCOM061", "BCOM062", "BCOM063", "BCOM064", "BCOM065", "BCOM066", "BCOM067", "BCOM068", "BCOM069", "BCOM070",
    "BCOM071", "BCOM072", "BCOM073", "BCOM074", "BCOM075", "BCOM076", "BCOM077", "BCOM078", "BCOM079", "BCOM080",
    "BCOM081", "BCOM082", "BCOM083", "BCOM084", "BCOM085", "BCOM086", "BCOM087", "BCOM088", "BCOM089", "BCOM090",
    "BCOM091", "BCOM092", "BCOM093", "BCOM094", "BCOM095", "BCOM096", "BCOM097", "BCOM098", "BCOM099", "BCOM100",
    "BCOM101", "BCOM102", "BCOM103", "BCOM104", "BCOM105", "BCOM106", "BCOM107", "BCOM108", "BCOM109", "BCOM110",
    "BCOM111", "BCOM112", "BCOM113", "BCOM114", "BCOM115", "BCOM116", "BCOM117", "BCOM118", "BCOM119", "BCOM120",
    "BCOM121", "BCOM122", "BCOM123", "BCOM124", "BCOM125", "BCOM126", "BCOM127", "BCOM128", "BCOM129", "BCOM130",
    "BCOM131", "BCOM132", "BCOM133", "BCOM134", "BCOM135", "BCOM136", "BCOM137", "BCOM138", "BCOM139", "BCOM140",
     "TA001", "TA002", "TA003", "TA004", "TA005", "TA006", "TA007", "TA008", "TA009", "TA010",
    "TA011", "TA012", "TA013", "TA014", "TA015", "TA016", "TA017", "TA018", "TA019", "TA020",
    "TA021", "TA022", "TA023", "TA024", "TA025", "TA026", "TA027", "TA028", "TA029", "TA030",
    "TA031", "TA032", "TA033", "TA034", "TA035", "TA036", "TA037", "TA038", "TA039", "TA040",
    "TA041", "TA042", "TA043", "TA044", "TA045", "TA046", "TA047", "TA048", "TA049", "TA050",
    "TA051", "TA052", "TA053", "TA054", "TA055", "TA056", "TA057", "TA058", "TA059", "TA060",
    "TA061", "TA062", "TA063", "TA064", "TA065", "TA066", "TA067", "TA068", "TA069", "TA070",
    "TA071", "TA072", "TA073", "TA074", "TA075", "TA076", "TA077", "TA078", "TA079", "TA080",
    "TA081", "TA082", "TA083", "TA084", "TA085", "TA086", "TA087", "TA088", "TA089", "TA090",
    "TA091", "TA092", "TA093", "TA094", "TA095", "TA096", "TA097", "TA098", "TA099", "TA100",
     "BIO001", "BIO002", "BIO003", "BIO004", "BIO005", "BIO006", "BIO007", "BIO008", "BIO009", "BIO010",
    "BIO011", "BIO012", "BIO013", "BIO014", "BIO015", "BIO016", "BIO017", "BIO018", "BIO019", "BIO020",
    "BIO021", "BIO022", "BIO023", "BIO024", "BIO025", "BIO026", "BIO027", "BIO028", "BIO029", "BIO030",
    "BIO031", "BIO032", "BIO033", "BIO034", "BIO035", "BIO036", "BIO037", "BIO038", "BIO039", "BIO040",
    "BIO041", "BIO042", "BIO043", "BIO044", "BIO045", "BIO046", "BIO047", "BIO048", "BIO049", "BIO050",
    "BIO051", "BIO052", "BIO053", "BIO054", "BIO055", "BIO056", "BIO057", "BIO058", "BIO059", "BIO060",
    "BIO061", "BIO062", "BIO063", "BIO064", "BIO065", "BIO066", "BIO067", "BIO068", "BIO069", "BIO070",
    "BCOMCA021", "BCOMCA022", "BCOMCA023", "BCOMCA024", "BCOMCA025", "BCOMCA026", "BCOMCA027", "BCOMCA028", "BCOMCA029", "BCOMCA030",
    "BCOMCA031", "BCOMCA032", "BCOMCA033", "BCOMCA034", "BCOMCA035", "BCOMCA036", "BCOMCA037", "BCOMCA038", "BCOMCA039", "BCOMCA040",
    "BCOMCA041", "BCOMCA042", "BCOMCA043", "BCOMCA044", "BCOMCA045", "BCOMCA046", "BCOMCA047", "BCOMCA048", "BCOMCA049", "BCOMCA050",
    "BCOMCA051", "BCOMCA052", "BCOMCA053", "BCOMCA054", "BCOMCA055", "BCOMCA056", "BCOMCA057", "BCOMCA058", "BCOMCA059", "BCOMCA060",
    "BCOMCA061", "BCOMCA062", "BCOMCA063", "BCOMCA064", "BCOMCA065", "BCOMCA066", "BCOMCA067", "BCOMCA068", "BCOMCA069", "BCOMCA070",
    "BCOMCA071", "BCOMCA072", "BCOMCA073", "BCOMCA074", "BCOMCA075", "BCOMCA076", "BCOMCA077", "BCOMCA078", "BCOMCA079", "BCOMCA080",
    "BCOMCA081", "BCOMCA082", "BCOMCA083", "BCOMCA084", "BCOMCA085", "BCOMCA086", "BCOMCA087", "BCOMCA088", "BCOMCA089", "BCOMCA090",
    "BCOMCA091", "BCOMCA092", "BCOMCA093", "BCOMCA094", "BCOMCA095", "BCOMCA096", "BCOMCA097", "BCOMCA098", "BCOMCA099", "BCOMCA100",
    "BCOMCA101", "BCOMCA102", "BCOMCA103", "BCOMCA104", "BCOMCA105", "BCOMCA106", "BCOMCA107", "BCOMCA108", "BCOMCA109", "BCOMCA110",
    "BCOMCA111", "BCOMCA112", "BCOMCA113", "BCOMCA114", "BCOMCA115", "BCOMCA116", "BCOMCA117", "BCOMCA118", "BCOMCA119", "BCOMCA120",
    "BCOMCA121", "BCOMCA122", "BCOMCA123", "BCOMCA124", "BCOMCA125", "BCOMCA126", "BCOMCA127", "BCOMCA128", "BCOMCA129", "BCOMCA130",
    "BCOMCA131", "BCOMCA132", "BCOMCA133", "BCOMCA134", "BCOMCA135", "BCOMCA136", "BCOMCA137", "BCOMCA138", "BCOMCA139", "BCOMCA140"
]
rows_per_class = 5
total_classes = 32
total_students = rows_per_class * total_classes

# Reset indices
d1 = 0
d2 = len(l2) - 1

# Iterate to populate the list of rows
class_dfs = []
for class_num in range(1, total_classes + 1):
    # Add the class number to the first row
    class_row = [f"CLASS {class_num}"] + [""] * 7

    rows = [class_row]

    for student_num in range(1, rows_per_class + 1):
        row_data = []
        for x in range(1, 4 + 1):
            # Take values alternately from l1 and l2
            value_from_l1 = l1[d1 % len(l1)]
            value_from_l2 = l2[d2 % len(l2)]

            # Append the values to the row_data list
            row_data.extend([value_from_l1, value_from_l2])

            # Increment indices for the next iteration
            d1 += 1
            d2 -= 1

        # Append the row_data to the list of rows
        rows.append(row_data)

    # Transpose the rows to switch from row-wise to column-wise
    class_df = pd.DataFrame(rows).transpose()

    # Set the first row as the column headers
    class_df.columns = class_df.iloc[0]

    # Drop the first row (class_row) as it is now used as column headers
    class_df = class_df[1:]

    # Exclude the first column from being treated as headers
    class_df = class_df.iloc[:, 1:]

    # Limit the rows to 5 for each class
    class_df = class_df.iloc[:7]

    # Append the class DataFrame to the list of class DataFrames
    class_dfs.append(class_df)

# Concatenate the class DataFrames along columns
final_df = pd.concat(class_dfs, axis=1)

# Save the final DataFrame to an Excel file
final_df.to_excel("output_switched_5rows_with_header.xlsx", index=False)
