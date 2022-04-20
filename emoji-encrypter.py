emoji_encode={'a':'😀','b':'😃','c':'😄','d':'😁','e':'😆','f':'😅','g':'😂','h':'🤣','i':'😊','j':'😇','k':'🙂','l':'🙃','m':'😉','n':'😌',
'ñ':'😍','o':'🥰','p':'😘','q':'😗','r':'😙','s':'😚','t':'😋','u':'😛','v':'😝','w':'😜','x':'🤪','y':'🤨','z':'🧐','!':'🤓',
'#':'😎','$':'🤩','%':'🥳','&':'😏','/':'😒','(':'😞',')':'😔','?':'😟','¡':'😕','¿':'🙁','.':'😣','_':'😖','+':'😫','=':'😩','-':'🥺','*':'😢','<':'😭','>':'😤','|':'😠','{':'😡','}':'🤬','[':'🤯',']':'😳','^':'🥵','~':'🥶',';':'😱',':':'😨','"':'😰',"'":'😥'}

emoji_decode={'😀':'a','😃':'b','😄':'c','😁':'d','😆':'e','😅':'f','😂':'g','🤣':'h','😊':'i','😇':'j','🙂':'k','🙃':'l','😉':'m','😌':'n',
'😍':'ñ','🥰':'o','😘':'p','😗':'q','😙':'r','😚':'s','😋':'t','😛':'u','😝':'v','😜':'w','🤪':'x','🤨':'y','🧐':'z','🤓':'!',
'😎':'#','🤩':'$','🥳':'%','😏':'&','😒':'/','😞':'(','😔':')','😟':'?','😕':'¡','🙁':'¿','😣':'.','😖':'_','😫':'+','😩':'=','':'-','😢':'*','😭':'<','😤':'>','😠':'|','😡':'{','🤬':'}','🤯':'[','😳':']','🥵':'^','🥶':'~','😱':';','😨':':','😰':'"','😥':"'"}

encode_string = []
decode_string = []

def encode(string):
    for i in string.lower():
        if i in emoji_encode:
            encode_string.append(emoji_encode[i])
        else:
            encode_string.append(i)
    output = "".join(encode_string)
    return output

def decode(string):
    for i in string.lower():
        if i in emoji_decode:
            decode_string.append(emoji_decode[i])
        else:
            decode_string.append(i)
    output = "".join(decode_string)
    return output

print(encode("The best encrypter ever made!!!"))
print(decode("🤣😆🙃🙃🥰 🧐😊😘😘😆😁😚😄😙😊😘😋🤓"))

