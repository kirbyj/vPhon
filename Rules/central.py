#central.py
#coding: utf-8

onsets = { u'b' : u'b', u't' : u't', u'th' : u'tʰ', u'đ' : u'd', u'ch' : u'c', 
u'kh' : u'x', u'g' : u'ɣ', u'l' : u'l', u'm' : u'm', u'n': u'n', 
u'ngh': u'ŋ', u'nh' : u'ɲ', u'ng' : u'ŋ', u'ph' : u'f', u'v' : u'j', 
u'x' : u's', u'd' : u'j', u'h' : u'h', u'p' : u'p', u'qu' : u'w',
u'gi' : u'j', u'tr' : u'ʈ', u'k' : u'k', u'c' : u'k', u'gh' : u'ɣ',
u'r' : u'ʐ', u's' : u'ʂ', u'gi' : u'j'
}
			  
nuclei = { u'a' : u'a', u'á' : u'a', u'à' : u'a', u'ả' : u'a', u'ã' : u'a', u'ạ' : u'a', 
u'â' : u'ɤ̆', u'ấ' : u'ɤ̆', u'ầ' : u'ɤ̆', u'ẩ' : u'ɤ̆', u'ẫ' : u'ɤ̆', u'ậ' : u'ɤ̆',
u'ă' : u'ă', u'ắ' : u'ă', u'ằ' : u'ă', u'ẳ' : u'ă', u'ẵ' : u'ă', u'ặ' : u'ă',
u'e' : u'ɛ', u'é' : u'ɛ', u'è' : u'ɛ', u'ẻ' : u'ɛ', u'ẽ' : u'ɛ', u'ẹ' : u'ɛ',
u'ê' : u'e', u'ế' : u'e', u'ề' : u'e', u'ể' : u'e', u'ễ' : u'e', u'ệ' : u'e',
u'i' : u'i', u'í' : u'i', u'ì' : u'i', u'ỉ' : u'i', u'ĩ' : u'i', u'ị' : u'i',
u'o' : u'ɔ', u'ó' : u'ɔ', u'ò' : u'ɔ', u'ỏ' : u'ɔ', u'õ' : u'ɔ', u'ọ' : u'ɔ',
u'ô' : u'o', u'ố' : u'o', u'ồ' : u'o', u'ổ' : u'o', u'ỗ' : u'o', u'ộ' : u'o',
u'ơ' : u'ɤ', u'ớ' : u'ɤ', u'ờ' : u'ɤ', u'ở' : u'ɤ', u'ỡ' : u'ɤ', u'ợ' : u'ɤ',
u'u' : u'u', u'ú' : u'u', u'ù' : u'u', u'ủ' : u'u', u'ũ' : u'u', u'ụ' : u'u',
u'ư' : u'ɯ', u'ứ' : u'ɯ', u'ừ' : u'ɯ', u'ử' : u'ɯ', u'ữ' : u'ɯ', u'ự' : u'ɯ',
u'y' : u'i', u'ý' : u'i', u'ỳ' : u'i', u'ỷ' : u'i', u'ỹ' : u'i', u'ỵ' : u'i',
				
u'eo' : u'eo', u'éo' : u'eo', u'èo' : u'eo', u'ẻo' : u'eo', u'ẽo': u'eo', u'ẹo' : u'eo',
u'êu' : u'ɛu', u'ếu' : u'ɛu', u'ều' : u'ɛu', u'ểu' : u'ɛu', u'ễu': u'ɛu', u'ệu' : u'ɛu',
u'ia' : u'iə', u'ía' : u'iə', u'ìa' : u'iə', u'ỉa' : u'iə', u'ĩa' : u'iə', u'ịa' : u'iə',
u'ia' : u'iə', u'iá' : u'iə', u'ià' : u'iə', u'iả' : u'iə', u'iã' : u'iə', u'iạ' : u'iə',
u'iê' : u'iə', u'iế' : u'iə', u'iề' : u'iə', u'iể' : u'iə', u'iễ' : u'iə', u'iệ' : u'iə',
u'oo' : u'ɔ', u'óo' : u'ɔ', u'òo' : u'ɔ', u'ỏo' : u'ɔ', u'õo' : u'ɔ', u'ọo' : u'ɔ',
u'oo' : u'ɔ', u'oó' : u'ɔ', u'oò' : u'ɔ', u'oỏ' : u'ɔ', u'oõ' : u'ɔ', u'oọ' : u'ɔ',
u'ôô' : u'o', u'ốô' : u'o', u'ồô' : u'o', u'ổô' : u'o', u'ỗô' : u'o', u'ộô' : u'o',				                 
u'ôô' : u'o', u'ôố' : u'o', u'ôồ' : u'o', u'ôổ' : u'o', u'ôỗ' : u'o', u'ôộ' : u'o',				                  
u'ua' : u'uə', u'úa' : u'uə', u'ùa' : u'uə', u'ủa' : u'uə', u'ũa' : u'uə', u'ụa' : u'uə',
u'uô' : u'uə', u'uố' : u'uə', u'uồ' : u'uə', u'uổ' : u'uə', u'uỗ' : u'uə', u'uộ' : u'uə',
u'ưa' : u'ɯə', u'ứa' : u'ɯə', u'ừa' : u'ɯə', u'ửa' : u'ɯə', u'ữa' : u'ɯə', u'ựa' : u'ɯə',
u'ươ' : u'ɯə', u'ướ' : u'ɯə', u'ườ' : u'ɯə', u'ưở' : u'ɯə', u'ưỡ' : u'ɯə', u'ượ' : u'ɯə',
u'yê' : u'iɛ', u'yế' : u'iɛ', u'yề' : u'iɛ', u'yể' : u'iɛ', u'yễ' : u'iɛ', u'yệ' : u'iɛ', 
u'uơ' : u'uə',  u'uở' : u'uə', u'uờ': u'uə', u'uở' : u'uə', u'uỡ' : u'uə', u'uợ' : u'uə',
}
				         
offglides =  { u'ai' : u'aj', u'ái' : u'aj', u'ài' : u'aj', u'ải' : u'aj', u'ãi' : u'aj', u'ại' : u'aj',
u'ay' : u'ăj', u'áy' : u'ăj', u'ày' : u'ăj', u'ảy' : u'ăj', u'ãy' : u'ăj', u'ạy' : u'ăj',
u'ao' : u'aw', u'áo' : u'aw', u'ào' : u'aw', u'ảo' : u'aw', u'ão' : u'aw', u'ạo' : u'aw',
u'au' : u'ăw', u'áu' : u'ăw', u'àu' : u'ăw', u'ảu' : u'ăw', u'ãu' : u'ăw', u'ạu' : u'ăw',
u'ây' : u'ɤ̆j',  u'ấy' : u'ɤ̆j',  u'ầy' : u'ɤ̆j', u'ẩy' : u'ɤ̆j', u'ẫy' : u'ɤ̆j', u'ậy' : u'ɤ̆j', 
u'âu' : u'ɤ̆w', u'ấu' : u'ɤ̆w', u'ầu': u'ɤ̆w', u'ẩu' : u'ɤ̆w', u'ẫu' : u'ɤ̆w', u'ậu' : u'ɤ̆w',
u'eo' : u'ew', u'éo' : u'ew', u'èo' : u'ew', u'ẻo' : u'ew', u'ẽo' : u'ew', u'ẹo' : u'ew',
u'iu' : u'iw', u'íu' : u'iw', u'ìu' : u'iw', u'ỉu' : u'iw', u'ĩu' : u'iw', u'ịu' : u'iw',
u'oi' : u'ɔj', u'ói' : u'ɔj', u'òi' : u'ɔj', u'ỏi' : u'ɔj', u'õi' : u'ɔj', u'ọi' : u'ɔj',
u'ôi' : u'oj', u'ối' : u'oj', u'ồi' : u'oj', u'ổi' : u'oj', u'ỗi' : u'oj', u'ội' : u'oj',
u'ui' : u'uj', u'úi' : u'uj', u'ùi' : u'uj', u'ủi' : u'uj', u'ũi' : u'uj', u'ụi' : u'uj', 
u'uy' : u'uj', u'úy' : u'uj', u'ùy' : u'uj', u'ủy' : u'uj', u'ũy' : u'uj', u'ụy' : u'uj', 
u'ơi' : u'ɤj', u'ới' : u'ɤj', u'ời' : u'ɤj', u'ởi' : u'ɤj', u'ỡi' : u'ɤj', u'ợi' : u'ɤj', 
u'ưi' : u'ɯj', u'ứi' : u'ɯj', u'ừi' : u'ɯj', u'ửi' : u'ɯj', u'ữi' : u'ɯj', u'ựi' : u'ɯj', 
u'ưu' : u'ɯw', u'ứu' : u'ɯw', u'ừu' : u'ɯw', u'ửu' : u'ɯw', u'ữu' : u'ɯw', u'ựu' : u'ɯw',

u'iêu' : u'iəw', u'iếu' : u'iəw', u'iều' : u'iəw', u'iểu' : u'iəw', u'iễu' : u'iəw', u'iệu' : u'iəw',
u'yêu' : u'iəw', u'yếu' : u'iəw', u'yều' : u'iəw', u'yểu' : u'iəw', u'yễu' : u'iəw', u'yệu' : u'iəw', 
u'uôi' : u'uəj', u'uối' : u'uəj', u'uồi' : u'uəj', u'uổi' : u'uəj', u'uỗi' : u'uəj', u'uội' : u'uəj', 
u'ươi' : u'ɯəj', u'ưới' : u'ɯəj', u'ười' : u'ɯəj', u'ưởi' : u'ɯəj', u'ưỡi' : u'ɯəj', u'ượi' : u'ɯəj', 
u'ươu' : u'ɯəw', u'ướu' : u'ɯəw', u'ườu' : u'ɯəw', u'ưởu' : u'ɯəw', 'ưỡu' : u'ɯəw', u'ượu' : u'ɯəw'	 
}
				
onglides =   { u'oa' : u'a', u'oá' : u'a', u'oà' : u'a', u'oả' : u'a', u'oã' : u'a', u'oạ' : u'a', 
u'óa' : u'a', u'òa' : u'a', u'ỏa' : u'a', u'õa' : u'a', u'ọa' : u'a', 
u'oă' : u'ă', u'oắ' : u'ă', u'oằ' : u'ă', u'oẳ' : u'ă', u'oẵ' : u'ă', u'oặ' : u'ă', 	
u'oe' : u'e', u'oé' : u'e', u'oè' : u'e', u'oẻ' : u'e', u'oẽ' : u'e', u'oẹ' : u'e', 	
u'oe' : u'e', u'óe' : u'e', u'òe' : u'e', u'ỏe' : u'e', u'õe' : u'e', u'ọe' : u'e', 	
u'ua' : u'a', u'uá' : u'a', u'uà' : u'a', u'uả' : u'a', u'uã' : u'a', u'uạ' : u'a', 
u'uă' : u'ă', u'uắ' : u'ă', u'uằ' : u'ă', u'uẳ' : u'ă', u'uẵ' : u'ă', u'uặ' : u'ă', 	
u'uâ' : u'ɤ̆', u'uấ' : u'ɤ̆', u'uầ' : u'ɤ̆', u'uẩ' : u'ɤ̆', u'uẫ' : u'ɤ̆', u'uậ' : u'ɤ̆', 
u'ue' : u'ɛ', u'ué' : u'ɛ', u'uè' : u'ɛ', u'uẻ' : u'ɛ', u'uẽ' : u'ɛ', u'uẹ' : u'ɛ', 
u'uê' : u'e', u'uế' : u'e', u'uề' : u'e', u'uể' : u'e', u'uễ' : u'e', u'uệ' : u'e', 
u'uơ' : u'ɤ', u'uớ' : u'ɤ', u'uờ' : u'ɤ', u'uở' : u'ɤ', u'uỡ' : u'ɤ', u'uợ' : u'ɤ', 
u'uy' : u'i', u'uý' : u'i', u'uỳ' : u'i', u'uỷ' : u'i', u'uỹ' : u'i', u'uỵ' : u'i',
u'uya' : u'iə', u'uyá' : u'iə', u'uyà' : u'iə', u'uyả' : u'iə', u'uyã' : u'iə', u'uyạ' : u'iə', 
u'uyê' : u'iə', u'uyế' : u'iə', u'uyề' : u'iə', u'uyể' : u'iə', u'uyễ' : u'iə', u'uyệ' : u'iə', 
u'uyu' : u'iu', u'uyú' : u'iu', u'uyù' : u'iu', u'uyủ' : u'iu', u'uyũ' : u'iu', u'uyụ' : u'iu', 
u'uyu' : u'iu', u'uýu' : u'iu', u'uỳu' : u'iu', u'uỷu' : u'iu', u'uỹu' : u'iu', u'uỵu' : u'iu',
u'oen' : u'en', u'oén' : u'en', u'oèn' : u'en', u'oẻn' : u'en', u'oẽn' : u'en', u'oẹn' : u'en', 	
u'oet' : u'et', u'oét' : u'et', u'oèt' : u'et', u'oẻt' : u'et', u'oẽt' : u'et', u'oẹt' : u'et' 	
}

onoffglides = { u'oe' : u'ej', u'oé' : u'ej', u'oè' : u'ej', u'oẻ' : u'ej', u'oẽ' : u'ej', u'oẹ' : u'ej', 
u'oai' : u'aj', u'oái' : u'aj', u'oài' : u'aj', u'oải' : u'aj', u'oãi' : u'aj', u'oại' : u'aj',
u'oay' : u'ăj', u'oáy' : u'ăj', u'oày' : u'ăj', u'oảy' : u'ăj', u'oãy' : u'ăj', u'oạy' : u'ăj',
u'oao' : u'aw', u'oáo' : u'aw', u'oào' : u'aw', u'oảo' : u'aw', u'oão' : u'aw', u'oạo' : u'aw',
u'oeo' : u'ew', u'oéo' : u'ew', u'oèo' : u'ew', u'oẻo' : u'ew', u'oẽo' : u'ew', u'oẹo' : u'ew',
u'oeo' : u'ew', u'óeo' : u'ew', u'òeo' : u'ew', u'ỏeo' : u'ew', u'õeo' : u'ew', u'ọeo' : u'ew',
u'ueo' : u'ew', u'uéo' : u'ew', u'uèo' : u'ew', u'uẻo' : u'ew', u'uẽo' : u'ew', u'uẹo' : u'ew',
u'uai' : u'aj', u'uái' : u'aj', u'uài' : u'aj', u'uải' : u'aj', u'uãi' : u'aj', u'uại' : u'aj',
u'uay' : u'ăj', u'uáy' : u'ăj', u'uày' : u'ăj', u'uảy' : u'ăj', u'uãy' : u'ăj', u'uạy' : u'ăj',
u'uây' : u'ɤ̆j', u'uấy' : u'ɤ̆j', u'uầy' : u'ɤ̆j', u'uẩy' : u'ɤ̆j', u'uẫy' : u'ɤ̆j', u'uậy' : u'ɤ̆j'
}

codas = { u'p' : u'p', u't' : u'k', u'c' : u'k', u'm' : u'm', u'n' : u'ŋ', u'ng' : u'ŋ', u'nh' : u'n', u'ch' : u'k' }

# See Alves 2007 (SEALS XII), Vũ 1982
tones = { u'á' : 13, u'à' : 42, u'ả' : 312, u'ã' : 312, u'ạ' : u'21g', 
          u'ấ' : 13, u'ầ' : 42, u'ẩ' : 312, u'ẫ' : 312, u'ậ' : u'21g',
          u'ắ' : 13, u'ằ' : 42, u'ẳ' : 312, u'ẵ' : 312, u'ặ' : u'21g',
          u'é' : 13, u'è' : 42, u'ẻ' : 312, u'ẽ' : 312, u'ẹ' : u'21g',
          u'ế' : 13, u'ề' : 42, u'ể' : 312, u'ễ' : 312, u'ệ' : u'21g',
          u'í' : 13, u'ì' : 42, u'ỉ' : 312, u'ĩ' : 312, u'ị' : u'21g',
          u'ó' : 13, u'ò' : 42, u'ỏ' : 312, u'õ' : 312, u'ọ' : u'21g',
          u'ố' : 13, u'ồ' : 42, u'ổ' : 312, u'ỗ' : 312, u'ộ' : u'21g',
          u'ớ' : 13, u'ờ' : 42, u'ở' : 312, u'ỡ' : 312, u'ợ' : u'21g',
          u'ú' : 13, u'ù' : 42, u'ủ' : 312, u'ũ' : 312, u'ụ' : u'21g',
          u'ứ' : 13, u'ừ' : 42, u'ử' : 312, u'ữ' : 312, u'ự' : u'21g',
          u'ý' : 13, u'ỳ' : 42, u'ỷ' : 312, u'ỹ' : 312, u'ỵ' : u'21g',
          }

# used to use \u02C0 for raised glottal instead of g

tones_p = { u'á' : 5, u'à' : 2, u'ả' : 4, u'ã' : 4, u'ạ' : 6,
u'ấ' : 5, u'ầ' : 2, u'ẩ' : 4, u'ẫ' : 4, u'ậ' : 6,
u'ắ' : 5, u'ằ' : 2, u'ẳ' : 4, u'ẵ' : 4, u'ặ' : 6,
u'é' : 5, u'è' : 2, u'ẻ' : 4, u'ẽ' : 4, u'ẹ' : 6,
u'ế' : 5, u'ề' : 2, u'ể' : 4, u'ễ' : 4, u'ệ' : 6,
u'í' : 5, u'ì' : 2, u'ỉ' : 4, u'ĩ' : 4, u'ị' : 6,
u'ó' : 5, u'ò' : 2, u'ỏ' : 4, u'õ' : 4, u'ọ' : 6,
u'ố' : 5, u'ồ' : 2, u'ổ' : 4, u'ỗ' : 4, u'ộ' : 6,
u'ớ' : 5, u'ờ' : 2, u'ở' : 4, u'ỡ' : 4, u'ợ' : 6, 
u'ú' : 5, u'ù' : 2, u'ủ' : 4, u'ũ' : 4, u'ụ' : 6,
u'ứ' : 5, u'ừ' : 2, u'ử' : 4, u'ữ' : 4, u'ự' : 6, 
u'ý' : 5, u'ỳ' : 2, u'ỷ' : 4, u'ỹ' : 4, u'ỵ' : 6,
}

gi = { u'gi' : u'ji', u'gí': u'ji', u'gì' : u'ji', u'gì' : u'ji', u'gĩ' : u'ji', u'gị' : u'ji' }

qu = {u'quy' : u'wi', u'qúy' : u'wi', u'qùy' : u'wi', u'qủy' : u'wi', u'qũy' : u'wi', u'qụy' : u'wi'}
