﻿#rules.py
#coding: utf-8

onsets = {  'b' : 'ɓ', 
            'c' : 'k', 
            'ch' : 'c',
            'd' : 'j',
            'đ' : 'ɗ', 
            'g' : 'ɣ',
            'gh' : 'ɣ', 
            'gi' : 'z',
            'h' : 'h',
            'k' : 'k', 
            'kh' : 'x', 
            'l' : 'l',
            'm' : 'm',
            'n' : 'n',
            'ng' : 'ŋ',
            'ngh' : 'ŋ',
            'nh' : 'ɲ',
            'ph' : 'f',
            'p' : 'p',
            'qu' : 'kʷ',
            'r' : 'r',
            's' : 'ʂ',
            't' : 't',
            'th' : 'tʰ', 
            'tr' : 'ʈ',
            'v' : 'v', 
            'x' : 's'}

gi = { 'gi' : 'zi', 'gí': 'zi', 'gì' : 'zi', 'gỉ' : 'zi', 'gĩ' : 'zi', 'gị' : 'zi'}

qu = {'quy' : 'kʷi', 'quý' : 'kʷi', 'quỳ' : 'kʷi', 'quỷ' : 'kʷi', 'quỹ' : 'kʷi', 'quỵ' : 'kʷi'}

nuclei = {  'a' : 'aː', 'á' : 'aː', 'à' : 'aː', 'ả' : 'aː', 'ã' : 'aː', 'ạ' : 'aː',
            'â' : 'ə', 'ấ' : 'ə', 'ầ' : 'ə', 'ẩ' : 'ə', 'ẫ' : 'ə', 'ậ' : 'ə',
            'ă' : 'a', 'ắ' : 'a', 'ằ' : 'a', 'ẳ' : 'a', 'ẵ' : 'a', 'ặ' : 'a',
	    'e' : 'ɛ', 'é' : 'ɛ', 'è' : 'ɛ', 'ẻ' : 'ɛ', 'ẽ' : 'ɛ', 'ẹ' : 'ɛ',
	    'ê' : 'e', 'ế' : 'e', 'ề' : 'e', 'ể' : 'e', 'ễ' : 'e', 'ệ' : 'e',
	    'i' : 'i', 'í' : 'i', 'ì' : 'i', 'ỉ' : 'i', 'ĩ' : 'i', 'ị' : 'i',
	    'o' : 'ɔ', 'ó' : 'ɔ', 'ò' : 'ɔ', 'ỏ' : 'ɔ', 'õ' : 'ɔ', 'ọ' : 'ɔ',
	    'ô' : 'o', 'ố' : 'o', 'ồ' : 'o', 'ổ' : 'o', 'ỗ' : 'o', 'ộ' : 'o',
	    'ơ' : 'əː', 'ớ' : 'əː', 'ờ' : 'əː', 'ở' : 'əː', 'ỡ' : 'əː', 'ợ' : 'əː',
	    'u' : 'u', 'ú' : 'u', 'ù' : 'u', 'ủ' : 'u', 'ũ' : 'u', 'ụ' : 'u',
	    'ư' : 'ɨ', 'ứ' : 'ɨ', 'ừ' : 'ɨ', 'ử' : 'ɨ', 'ữ' : 'ɨ', 'ự' : 'ɨ',
	    'y' : 'i', 'ý' : 'i', 'ỳ' : 'i', 'ỷ' : 'i', 'ỹ' : 'i', 'ỵ' : 'i',
	    'ia' : 'iə', 'ía' : 'iə', 'ìa' : 'iə', 'ỉa' : 'iə', 'ĩa' : 'iə', 'ịa' : 'iə',
	    'ia' : 'iə', 'iá' : 'iə', 'ià' : 'iə', 'iả' : 'iə', 'iã' : 'iə', 'iạ' : 'iə',
	    'iê' : 'iə', 'iế' : 'iə', 'iề' : 'iə', 'iể' : 'iə', 'iễ' : 'iə', 'iệ' : 'iə',
	    'oo' : 'ɔː', 'óo' : 'ɔː', 'òo' : 'ɔː', 'ỏo' : 'ɔː', 'õo' : 'ɔː', 'ọo' : 'ɔː',
	    'oo' : 'ɔː', 'oó' : 'ɔː', 'oò' : 'ɔː', 'oỏ' : 'ɔː', 'oõ' : 'ɔː', 'oọ' : 'ɔː', 
            'ôô' : 'oː', 'ốô' : 'oː', 'ồô' : 'oː', 'ổô' : 'oː', 'ỗô' : 'oː', 'ộô' : 'oː', 
            'ôô' : 'oː', 'ôố' : 'oː', 'ôồ' : 'oː', 'ôổ' : 'oː', 'ôỗ' : 'oː', 'ôộ' : 'oː', 
            'ua' : 'uə', 'úa' : 'uə', 'ùa' : 'uə', 'ủa' : 'uə', 'ũa' : 'uə', 'ụa' : 'uə',
	    'uô' : 'uə', 'uố' : 'uə', 'uồ' : 'uə', 'uổ' : 'uə', 'uỗ' : 'uə', 'uộ' : 'uə',
	    'ưa' : 'ɨə', 'ứa' : 'ɨə', 'ừa' : 'ɨə', 'ửa' : 'ɨə', 'ữa' : 'ɨə', 'ựa' : 'ɨə',
	    'ươ' : 'ɨə', 'ướ' : 'ɨə', 'ườ' : 'ɨə', 'ưở' : 'ɨə', 'ưỡ' : 'ɨə', 'ượ' : 'ɨə',
	    'yê' : 'iə', 'yế' : 'iə', 'yề' : 'iə', 'yể' : 'iə', 'yễ' : 'iə', 'yệ' : 'iə', 
            'uơ' : 'uə',  'uở' : 'uə', 'uờ': 'uə', 'uở' : 'uə', 'uỡ' : 'uə', 'uợ' : 'uə'
	}
				         
offglides =  {  'ai' : 'aːj', 'ái' : 'aːj', 'ài' : 'aːj', 'ải' : 'aːj', 'ãi' : 'aːj', 'ại' : 'aːj',
                'ay' : 'aj', 'áy' : 'aj', 'ày' : 'aj', 'ảy' : 'aj', 'ãy' : 'aj', 'ạy' : 'aj',
                'ao' : 'aːw', 'áo' : 'aːw', 'ào' : 'aːw', 'ảo' : 'aːw', 'ão' : 'aːw', 'ạo' : 'aːw',
                'au' : 'aw', 'áu' : 'aw', 'àu' : 'aw', 'ảu' : 'aw', 'ãu' : 'aw', 'ạu' : 'aw',
                'ây' : 'əj', 'ấy' : 'əj', 'ầy' : 'əj', 'ẩy' : 'əj', 'ẫy' : 'əj', 'ậy' : 'əj',
                'âu' : 'əw', 'ấu' : 'əw', 'ầu' : 'əw', 'ẩu' : 'əw', 'ẫu' : 'əw', 'ậu' : 'əw',
                'eo' : 'ɛw', 'éo' : 'ɛw', 'èo' : 'ɛw', 'ẻo' : 'ɛw', 'ẽo' : 'ɛw', 'ẹo' : 'ɛw',
                'êu' : 'ew', 'ếu' : 'ew', 'ều' : 'ew', 'ểu' : 'ew', 'ễu' : 'ew', 'ệu' : 'ew',
                'iu' : 'iw', 'íu' : 'iw', 'ìu' : 'iw', 'ỉu' : 'iw', 'ĩu' : 'iw', 'ịu' : 'iw',
                'oi' : 'ɔj', 'ói' : 'ɔj', 'òi' : 'ɔj', 'ỏi' : 'ɔj', 'õi' : 'ɔj', 'ọi' : 'ɔj',
                'ôi' : 'oj', 'ối' : 'oj', 'ồi' : 'oj', 'ổi' : 'oj', 'ỗi' : 'oj', 'ội' : 'oj',
                'ui' : 'uj', 'úi' : 'uj', 'ùi' : 'uj', 'ủi' : 'uj', 'ũi' : 'uj', 'ụi' : 'uj',
                'uy' : 'uj', 'úy' : 'uj', 'ùy' : 'uj', 'ủy' : 'uj', 'ũy' : 'uj', 'ụy' : 'uj',
                'ơi' : 'əːj', 'ới' : 'əːj', 'ời' : 'əːj', 'ởi' : 'əːj', 'ỡi' : 'əːj', 'ợi' : 'əːj',
                'ưi' : 'ɨj', 'ứi' : 'ɨj', 'ừi' : 'ɨj', 'ửi' : 'ɨj', 'ữi' : 'ɨj', 'ựi' : 'ɨj',
                'ưu' : 'ɨw', 'ứu' : 'ɨw', 'ừu' : 'ɨw', 'ửu' : 'ɨw', 'ữu' : 'ɨw', 'ựu' : 'ɨw',
                'iêu' : 'iəw', 'iếu' : 'iəw', 'iều' : 'iəw', 'iểu' : 'iəw', 'iễu' : 'iəw', 'iệu' : 'iəw',
                'yêu' : 'iəw', 'yếu' : 'iəw', 'yều' : 'iəw', 'yểu' : 'iəw', 'yễu' : 'iəw', 'yệu' : 'iəw',
                'uôi' : 'uəj', 'uối' : 'uəj', 'uồi' : 'uəj', 'uổi' : 'uəj', 'uỗi' : 'uəj', 'uội' : 'uəj',
                'ươi' : 'ɨəj', 'ưới' : 'ɨəj', 'ười' : 'ɨəj', 'ưởi' : 'ɨəj', 'ưỡi' : 'ɨəj', 'ượi' : 'ɨəj',
                'ươu' : 'ɨəw', 'ướu' : 'ɨəw', 'ườu' : 'ɨəw', 'ưởu' : 'ɨəw', 'ưỡu' : 'ɨəw', 'ượu' : 'ɨəw'
               }

onglides =   {  'oa' : 'aː', 'oá' : 'aː', 'oà' : 'aː', 'oả' : 'aː', 'oã' : 'aː', 'oạ' : 'aː',
                             'óa' : 'aː', 'òa' : 'aː', 'ỏa' : 'aː', 'õa' : 'aː', 'ọa' : 'aː',
                'oă' : 'a', 'oắ' : 'a', 'oằ' : 'a', 'oẳ' : 'a', 'oẵ' : 'a', 'oặ' : 'a',
                'oe' : 'ɛ', 'oé' : 'ɛ', 'oè' : 'ɛ', 'oẻ' : 'ɛ', 'oẽ' : 'ɛ', 'oẹ' : 'ɛ',
                'oe' : 'ɛ', 'óe' : 'ɛ', 'òe' : 'ɛ', 'ỏe' : 'ɛ', 'õe' : 'ɛ', 'ọe' : 'ɛ',
                'ua' : 'aː', 'uá' : 'aː', 'uà' : 'aː', 'uả' : 'aː', 'uã' : 'aː', 'uạ' : 'aː',
                'uă' : 'a', 'uắ' : 'a', 'uằ' : 'a', 'uẳ' : 'a', 'uẵ' : 'a', 'uặ' : 'a',
                'uâ' : 'ə', 'uấ' : 'ə', 'uầ' : 'ə', 'uẩ' : 'ə', 'uẫ' : 'ə', 'uậ' : 'ə',
                'ue' : 'ɛ', 'ué' : 'ɛ', 'uè' : 'ɛ', 'uẻ' : 'ɛ', 'uẽ' : 'ɛ', 'uẹ' : 'ɛ',
                'uê' : 'e', 'uế' : 'e', 'uề' : 'e', 'uể' : 'e', 'uễ' : 'e', 'uệ' : 'e',
                'uy' : 'i', 'uý' : 'i', 'uỳ' : 'i', 'uỷ' : 'i', 'uỹ' : 'i', 'uỵ' : 'i',
                'uya' : 'iə', 'uyá' : 'iə', 'uyà' : 'iə', 'uyả' : 'iə', 'uyã' : 'iə', 'uyạ' : 'iə',
                'uyê' : 'iə', 'uyế' : 'iə', 'uyề' : 'iə', 'uyể' : 'iə', 'uyễ' : 'iə', 'uyệ' : 'iə',
                'oen' : 'ɛn', 'oén' : 'ɛn', 'oèn' : 'ɛn', 'oẻn' : 'ɛn', 'oẽn' : 'ɛn', 'oẹn' : 'ɛn',
                'oet' : 'ɛt', 'oét' : 'ɛt', 'oèt' : 'ɛt', 'oẻt' : 'ɛt', 'oẽt' : 'ɛt', 'oẹt' : 'ɛt'
                }

onoffglides = { 'oai' : 'aːj', 'oái' : 'aːj', 'oài' : 'aːj', 'oải' : 'aːj', 'oãi' : 'aːj', 'oại' : 'aːj',
                'oay' : 'aj', 'oáy' : 'aj', 'oày' : 'aj', 'oảy' : 'aj', 'oãy' : 'aj', 'oạy' : 'aj',
                'oao' : 'aw', 'oáo' : 'aw', 'oào' : 'aw', 'oảo' : 'aw', 'oão' : 'aw', 'oạo' : 'aw',
                'oeo' : 'ɛw', 'oéo' : 'ɛw', 'oèo' : 'ɛw', 'oẻo' : 'ɛw', 'oẽo' : 'ɛw', 'oẹo' : 'ɛw',
                'oeo' : 'ɛw', 'óeo' : 'ɛw', 'òeo' : 'ɛw', 'ỏeo' : 'ɛw', 'õeo' : 'ɛw', 'ọeo' : 'ɛw',
                'ueo' : 'ɛw', 'uéo' : 'ɛw', 'uèo' : 'ɛw', 'uẻo' : 'ɛw', 'uẽo' : 'ɛw', 'uẹo' : 'ɛw',
                'uêu' : 'ew', 'uếu' : 'ew', 'uều' : 'ew', 'uểu' : 'ew', 'uễu' : 'ew', 'uệu' : 'ew',
                'uyu' : 'iw', 'uyú' : 'iw', 'uyù' : 'iw', 'uyủ' : 'iw', 'uyũ' : 'iw', 'uyụ' : 'iw',
                'uyu' : 'iw', 'uýu' : 'iw', 'uỳu' : 'iw', 'uỷu' : 'iw', 'uỹu' : 'iw', 'uỵu' : 'iw',
                'uai' : 'aːj', 'uái' : 'aːj', 'uài' : 'aːj', 'uải' : 'aːj', 'uãi' : 'aːj', 'uại' : 'aːj',
                'uay' : 'aj', 'uáy' : 'aj', 'uày' : 'aj', 'uảy' : 'aj', 'uãy' : 'aj', 'uạy' : 'aj',
                'uây' : 'əj', 'uấy' : 'əj', 'uầy' : 'əj', 'uẩy' : 'əj', 'uẫy' : 'əj', 'uậy' : 'əj'
                }

codas = {   'c' : 'k', 
            'ch' : 'c',
            'k' : 'k',
            'm' : 'm', 
            'n' : 'n', 
            'ng' : 'ŋ', 
            'nh' : 'ɲ',
            'p' : 'p',
            't' : 't'}

tones =  {  'á' : 'B1', 'à' : 'A2', 'ả' : 'C1', 'ã' : 'C2', 'ạ' : 'B2', 
	    'ấ' : 'B1', 'ầ' : 'A2', 'ẩ' : 'C1', 'ẫ' : 'C2', 'ậ' : 'B2',
	    'ắ' : 'B1', 'ằ' : 'A2', 'ẳ' : 'C1', 'ẵ' : 'C2', 'ặ' : 'B2',
	    'é' : 'B1', 'è' : 'A2', 'ẻ' : 'C1', 'ẽ' : 'C2', 'ẹ' : 'B2',
	    'ế' : 'B1', 'ề' : 'A2', 'ể' : 'C1', 'ễ' : 'C2', 'ệ' : 'B2',
	    'í' : 'B1', 'ì' : 'A2', 'ỉ' : 'C1', 'ĩ' : 'C2', 'ị' : 'B2',
	    'ó' : 'B1', 'ò' : 'A2', 'ỏ' : 'C1', 'õ' : 'C2', 'ọ' : 'B2',
	    'ố' : 'B1', 'ồ' : 'A2', 'ổ' : 'C1', 'ỗ' : 'C2', 'ộ' : 'B2',
	    'ớ' : 'B1', 'ờ' : 'A2', 'ở' : 'C1', 'ỡ' : 'C2', 'ợ' : 'B2',
	    'ú' : 'B1', 'ù' : 'A2', 'ủ' : 'C1', 'ũ' : 'C2', 'ụ' : 'B2',
	    'ứ' : 'B1', 'ừ' : 'A2', 'ử' : 'C1', 'ữ' : 'C2', 'ự' : 'B2',
	    'ý' : 'B1', 'ỳ' : 'A2', 'ỷ' : 'C1', 'ỹ' : 'C2', 'ỵ' : 'B2'
	}

gedney_super = {'A1' : 'ᴬ¹', 'A2' : 'ᴬ²', 'B1' : 'ᴮ¹', 'B2' : 'ᴮ²', 'C1' : 'ᶜ¹', 'C2': 'ᶜ²', 'D1' : 'ᴰ¹', 'D2' : 'ᴰ²'} 

eight_super = {'A1' : '¹', 'A2' : '²', 'C1' : '³', 'C2' : '⁴', 'B1' : '⁵', 'B2': '⁶', 'D1' : '⁷', 'D2' : '⁸'} 

eight_lower = {'A1' : '1', 'A2' : '2', 'C1' : '3', 'C2' : '4', 'B1' : '5', 'B2': '6', 'D1' : '7', 'D2' : '8'} 

six_n_super = {'A1' : '¹', 'A2' : '²', 'C1' : '³', 'C2' : '⁴', 'B1' : '⁵', 'B2': '⁶', 'D1' : '⁵', 'D2' : '⁶'} 

six_n_lower = {'A1' : '1', 'A2' : '2', 'C1' : '3', 'C2' : '4', 'B1' : '5', 'B2': '6', 'D1' : '5', 'D2' : '6'} 

six_s_super = {'A1' : '¹', 'A2' : '²', 'C1' : '³', 'C2' : '³', 'B1' : '⁵', 'B2': '⁶', 'D1' : '⁵', 'D2' : '⁶'} 

six_s_lower = {'A1' : '1', 'A2' : '2', 'C1' : '3', 'C2' : '3', 'B1' : '5', 'B2': '6', 'D1' : '5', 'D2' : '6'} 

chao_n_super =  {'A1' : '³³', 'A2' : '³²', 'B1' : '²⁴', 'B2' : '²¹ˀ', 'C1' : '³¹²', 'C2' : '³ˀ⁵', 'D1' : '⁴⁵', 'D2' : '²¹'}

chao_n_lower =  {'A1' : '33', 'A2' : '32', 'B1' : '24', 'B2' : '21g', 'C1' : '312', 'C2' : '3g5', 'D1' : '45', 'D2' : '21'}

chao_c_super =  {'A1' : '³⁵', 'A2' : '⁴²', 'B1' : '²ˀ⁴', 'B2' : '³¹', 'C1' : '³²ˀ', 'C2' : '³²ˀ', 'D1' : '⁴⁵', 'D2' : '³¹'}

chao_c_lower =  {'A1' : '35', 'A2' : '42', 'B1' : '2g4', 'B2' : '31', 'C1' : '32g', 'C2' : '32g', 'D1' : '45', 'D2' : '31'}

chao_s_super =  {'A1' : '³³', 'A2' : '²¹', 'B1' : '⁴⁵', 'B2' : '²¹²', 'C1' : '²¹⁴', 'C2' : '²¹⁴', 'D1' : '⁴⁵', 'D2' : '²¹²'}

chao_s_lower =  {'A1' : '33', 'A2' : '21', 'B1' : '45', 'B2' : '212', 'C1' : '214', 'C2' : '214', 'D1' : '45', 'D2' : '212'}
