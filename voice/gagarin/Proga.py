import sys
import json
from itertools import count
z = 1
for a in sys.stdin:
    punc = '''!()-—[] {};:'"\,<>./?@#$%^&*_№~«»\n\r'''
    for ele in a:
        if ele in punc:
            a = a.replace(ele, "")
    a = a.lower()
    #print(a)
    if a==('васслышухорошо'):
        v = ('1.Vas_slishu_horosho.mp4')
    elif a==('васпонялприступатькпроверкескафандрачерез3минутысейчасзанят'):
        v = ('2.Vas_Ponyal.Pristupat_k_proverke.mp4')
    elif a==('проверкускафандразакончил'):
        v = ('3.Proverku_skafandra_zakonchil.mp4')
    elif a==('какменяслышите'):
        v = ('4.Kak_manya_slishite.mp4')
    elif a==('васслышуоченьслабоуменягоритсветозвуковаяпередачанадоскеочевиднопроисходитсписываниесмагнитофонакакменяпоняли'):
        v = ('5.Vas_slishu_ochen_slabo.mp4')
    elif a==('васнепонялвыключитепожалуйстамузыкуеслиможно'):
        v = ('6.Vas_ne_ponyal.Vikluchite_muziku.mp4')
    elif a==('всёсделанослышувасхорошо'):
        v = ('7.Vse_sdelano_slishu_vas_horosho.mp4')
    elif a==('работаюнадэмшдэмшдинамическийэлектромагнитныймикрофоншлемадаюсчет12345678910'):
        v = ('8.Rabotau_na_DEMSH.mp4')
    elif a==('васпонялпроверкасвязи12345678910какслышите'):
        v = ('9.Vas_ponyal_proverka_svayzi.mp4')
    elif a==('работаюнамагнитофоне12345678910васслышухорошоработаюнадэмш12345678910какпоняли'):
        v = ('10.Rabotayu_na_magnitofone.mp4')
    elif a==('приёмнателефон'):
        v = ('11.Priem_na_telefon.mp4')
    elif a==('чувствуюсебяпревосходнопроверкателефоновидинамиковнормальноперехожунателефон'):
        v = ('12.Chuvstvuyu_sebya_prevoshodno.mp4')
    elif a==('понялятакизнал'):
        v = ('13.Ponyal.Ya_tak_i_znal.mp4')
    elif a==('понялвассовершенноспокоен'):
        v = ('14.Ponyal_vas.Sovershenno_spokoen.mp4')
    elif a==('неслышалвёлвстречнуюпередачувсёвпорядкеговоритекакпоняли'):
        v = ('15.Ne_slishal.Vel_vstrechnuyu.mp4')
    elif a==('какучилисмех'):
        v = ('16.Kak_uchili.Ha_ha_ha.mp4')
    elif a==('понялландышсмехландышемназванкосмонавтпоповичпр'):
        v = ('17.Ponyal_landyish.mp4')
    elif a==('васпонялсейчасвашезаданиевыполню'):
        v = ('18.Vas_ponyal.Seychas_vashe_zadanie.mp4')
    elif a==('понялвасстартовоеположениеиприработенаорбитетумблернателеграфеиназареприразделениитумблернасигнал'):
        v = ('19.Ponyal_vas.Startovoe_polozhenie.mp4')
    elif a==('слышувасхорошокакменя'):
        v = ('20.Slishu_vas_horosho.mp4')
    elif a==('конечнояработойнеоченьзанят'):
        v = ('21.Konechno.mp4')
    elif a==('понялпонялпродолжай'):
        v = ('22.Ponyal_prodolzhai.mp4')
    elif a==('васпонялуменятожеидётвсехорошосамочувствиехорошеесейчасбудутзакрыватьлюк1'):
        v = ('23.Luk1.mp4')
    elif a==('васслышухорошонемножкопотишеговоритекакпоняли'):
        v = ('24.Potishe.mp4')
    elif a==('сейчасработалкнопкойнапультесейчасработаюкнопкойнаручкеуправленияработалсобеихкнопоквыслышитехорошокакпоняли'):
        v = ('25.Rabotal_na_pulte.mp4')
    elif a==('понялвасправильнопроверяюпользованиепамяткойивозможностьсчитываниясигналовпроверилвсёнормально'):
        v = ('26.Pamyatka.mp4')
    elif a==('понялвасбольшоеспасибопередайтеимсамыйгорячийотменя'):
        v = ('27.Goryachii.mp4')
    elif a==('понялподготовкаизделиянормальноуменятожесамочувствиеинастроениенормальнокстартуготов'):
        v = ('28.Podgotovka_izdeliya.mp4')
    elif a==('слышувасхорошознаюскемразговариваю'):
        v = ('29.Znayu_s_kem_razgovarivayu.mp4')
    elif a==('понялтакяидумал'):
        v = ('30.Tak_i_dumal.mp4')
    elif a==('прошудвадцатогонасвязьдвадцатыйкоролёв'):
        v = ('31.Proshu_dvadcatogo.mp4')
    elif a==('прошупринадёжнойсвязинаактивномучасткесообщитьвремяпозжеилираньшедосекундыстартаеслитаковоебудет'):
        v = ('32.Pri_nadezhnoi_svayzi.mp4')
    elif a==('понялвасправильнолюкоткрытпроверяютсигнализаторы'):
        v = ('33.Luk_otkrit.mp4')
    elif a==('работаюнадэмш'):
        v = ('34.Rabotayu_na_demsh.mp4')
    elif a==('васслышухорошокакменя'):
        v = ('20.Slishu_vas_horosho.mp4')
    elif a==('пакетпроверилдотянутьсялегкосвободнокакпоняли'):
        v = ('35.Paket_proveril.mp4')
    elif a==('уходаэтихвагоновнеслышубольношумбольшойслышувастолько'):
        v = ('36.Vagonyi.mp4')
    elif a==('васпонялобъявлена50минутнаяготовность'):
        v = ('37.50minut.mp4')
    elif a==('васслышухорошокрышкуужеочевиднокончаютзаворачивать'):
        v = ('38.Krishka.mp4')
    elif a==('уменятожевсёхорошосамочувствиехорошеенастроениебодрое'):
        v = ('39.U_menya_vse_horosho.mp4')
    elif a==('понялвас'):
        v = ('40.Ponyal_vas.mp4')
    elif a==('еслиестьмузычкаможнонемножкопустить'):
        v = ('41.Muzichka.mp4')
    elif a==('васпонялопускаютплощадкиобслуживаниянояшуманеслышунекоторыеколебанияощущаю'):
        v = ('42.Ploshadki.mp4')
    elif a==('покамузыкинетнонадеюсьсейчасбудет'):
        v = ('43.Muziki_net.mp4')
    elif a==('поканедали'):
        v = ('44.Poka_ne_dali.mp4')
    elif a==('далипролюбовь'):
        v = ('45.Dali_pro_lyubov.mp4')
    elif a==('музыкудаливсёхорошо'):
        v = ('46.Muziku_dali.mp4')
    elif a==('понялсердечныйприветимслушаюутесоваотдушиландыши'):
        v = ('47.Serdechniy_privet.mp4')
    elif a==('васпонялгерметичностьвпорядкеслышуинаблюдаюгерметичностьпроверилионичтототампостукиваютнемножко'):
        v = ('48.Germetichnost.mp4')
    elif a==('васслышухорошосамочувствиехорошеенастроениебодроекстартуготов'):
        v = ('49.K_startu_gotov.mp4')
    elif a==('хорошопролюбовьпоюттам'):
        v = ('50.Pro_lubov_pout.mp4')
    elif a==('васпонялуменятожевсёхорошоспокоенсамочувствиехорошееприветребятамвсёвремячувствуюиххорошуюдружескуюподдержкуонивместесомной'):
        v = ('51.Druzheskaya_podderzhka.mp4')
    elif a==('понялбольшоеспасибосердечноеспасибо'):
        v = ('52.Serdechnoe_spasibo.mp4')
    elif a==('доложилиправильносамочувствиехорошеенастроениебодроекдальнейшейработеготов'):
        v = ('53.Dolozhili_pravilno.mp4')
    elif a==('исходноеположениедлярегистрациифизиологическихфункцийзанял'):
        v = ('54.Fiziologicheskih_funkcii.mp4')
    elif a==('васпонялбудутотводитьустановщик'):
        v = ('55.Ustanovshik.mp4')
    elif a==('понялвасстрелаустановщикаотошланормально'):
        v = ('56.Strela_ustanovshika.mp4')
    elif a==('понялвассейчассостартапереходятвбункерминутныйперерывзатемпередачубудетеосуществлятьчерезних'):
        v = ('57.Bunker.mp4')
    elif a==('тожевсёпревосходнокакподанныммедицинысердцебьется'):
        v = ('58.Medicina.mp4')
    elif a==('понялзначитсердцебьётсякакаясейчасготовность'):
        v = ('59.Serdce_betsya.mp4')
    elif a==('васпонял15минутнаяготовностьодетьперчаткивыполняюперчаткиоделвсёнормально'):
        v = ('60.Perchatki_odel.mp4')
    elif a==('магнитофоннаавтоматическуюиручнуюзаписьнеработаеточевиднокончиласьплёнкапрошуперемотать'):
        v = ('61.Magnitofon.mp4')
    elif a==('понялвасидётперемоткапустьперемотаютвсюпленку'):
        v = ('62.Idet_peremotka.mp4')
    elif a==('васпонялобъявлена10минутнаяготовностьгермошлемзакрылвсёнормальносамочувствиехорошеекстартуготов'):
        v = ('63.Germoshlem.mp4')
    elif a==('васпонялобъявлена5минутнаяготовностьпоставитьгромкостьнаполнуюполнуюгромкостьввёл'):
        v = ('64.Gromkost.mp4')
    elif a==('васпонялвсеидётнормальнозанятьисходноеположениедлярегистрациифизиологическихфункцийположениезанял'):
        v = ('65.Polozhenie_zanayl.mp4')
    elif a==('яслышувасхорошоваспонялдоначалаоперацииосталосьещёпарочкаминутсамочувствиехорошеенастроениебодроекстартуготоввсёнормально'):
        v = ('66.Parochka_minut.mp4')
    elif a==('васпонялминутнаяготовностьзанималисходноеположениезанялпоэтомунесколькозадержалсясответом'):
        v = ('67.Minuta.mp4')
    elif not a == (''):
        v = ('999.Vas_ne_ponyal')
    c = {
        "video": v,
        "n": z
    }
    z = z+1
    b = json.dumps(c, indent=4)
    with open("demo.json", "w") as outfile:
        outfile.write(b)



