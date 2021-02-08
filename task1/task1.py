from json2table import convert
import json
my_file = None
'''with open("test.json", "r", encoding="utf-8") as f:
    my_file = json.load(f)
    build_direction = "LEFT_TO_RIGHT"
    table_attributes = {"style" : "width:100%; background:#AFCDE7; border-radius:10px;text-align: left;\
                        border-collapse: separate;border-spacing: 5px;border: 2px solid #ECE9E0;"}
    with open("test.html", "w") as w:
        c = convert(my_file, build_direction=build_direction, table_attributes=table_attributes)
        w.write(c)
        print(c)
'''
with open("test.json", "r", encoding="utf-8") as f:
    my_file = json.load(f)
    form = my_file["form"]
    items = form['items']
    with open("test1.html", "w") as w:
        def wr(text):
            w.write(text)
        wr('<div style="width:100%; border-radius:10px; text-align:center;\
                        border-spacing: 5px; border: 2px solid #ECE9E0;">')  
        #wr('<table>')
        wr("<h1>" + form["name"] + "</h1>")
        
        for i in range(len(items)):
            obj = items[i]
            if obj["type"] == "filler":
                atr = obj["attributes"]
                for key in atr.keys():
                    wr('<h3 type="filler">' + atr[key] + "</h3>")
            if obj["type"] in ["text", "textarea", "checkbox"]:
                atr = obj["attributes"]
                placeholder = atr.get("placeholder", None)
                required = atr["required"]
                label = atr["label"]
                clas = atr["class"]
                disabled = atr["disabled"]
                valRules = atr.get("validationRules", None)
                wr('<h3 type="text">' + atr['name'])
                
                if obj["type"] == "textarea":
                    wr("<textarea")
                    
                elif obj["type"] == "text":
                    wr("<input")
                    
                else:
                    wr("<input")
                    
                wr(' name="' + atr['name'] + '"')
                
                if obj["type"] != "checkbox":
                    value = atr["value"]
                    wr(' value="' + value +  '"')
                    
                else:
                    checked = atr['checked']
                    if checked:
                        wr(' checked')
                        
                if required:
                    wr(" required")
                '''else:
                    wr(" required=false")'''
                
                wr(' label="' + label + '"' + ' class="' + clas + '"')
                
                if not disabled:
                    wr(' disabled')
                '''else:
                    wr(' disabled')'''
                
                # валидация
                if valRules is not None:
                    wr(' type="' + valRules[0]["type"] + '"')
                else:
                    if obj["type"] == "checkbox":
                        wr(' type="checkbox"')
                        
                if placeholder is not None:
                    wr(' placeholder="' + placeholder + '"')
                    
                if obj["type"] == "textarea":
                    wr(">" + "</textarea>")
                elif obj["type"] == "text":
                    wr(">" + "</input>")
                else:
                    wr(">" + "</input>")
                    
                wr("</h3>")
                
            if obj["type"] == "button":
                atr = obj["attributes"]
                wr('<button class="' + atr["class"] + '">' + atr["text"])
                wr('</button>')
                
            if obj["type"] == "select":
                atr = obj["attributes"]
                options = atr['options']
                placeholder = atr.get("placeholder", None)
                required = atr["required"]
                label = atr["label"]
                clas = atr["class"]
                disabled = atr["disabled"]
                valRules = atr.get("validationRules", None)
                
                wr('<h3 type="text">' + atr['name'])
                wr("<select")
                wr(' name="' + atr['name'] + '"')
                value = atr["value"]
                wr(' value="' + value +  '"')
                
                if required:
                    wr(" required")
                wr(' label="' + label + '"' + ' class="' + clas + '"')
                
                if not disabled:
                    wr(' disabled')
                if valRules is not None:
                    wr(' type="' + valRules[0]["type"] + '"')
                
                if placeholder is not None:
                    wr(' placeholder="' + placeholder + '">')
                for i in range(len(options)):
                    wr('<option value="' + options[i]['value'] + '"')
                    if options[i]['selected']:
                        wr(' selected')                    
                    wr('>')
                    wr(options[i]['text'])
                    wr('</option>')
                wr("</select>")
                wr("</h3>")
            if obj["type"] == "radio":
                atr = obj["attributes"]
                item = atr['items']
                placeholder = atr.get("placeholder", None)
                required = atr["required"]
                label = atr["label"]
                clas = atr["class"]
                disabled = atr["disabled"]
                valRules = atr.get("validationRules", None)
                wr('<h3 type="text">' + atr['name'])
                wr('<input type="radio"')

                wr(' name="' + atr['name'] + '"')
                '''value = atr["value"]
                wr(' value="' + value +  '"')'''
                
                if required:
                    wr(" required")
                wr(' label="' + label + '"' + ' class="' + clas + '"')
                
                if not disabled:
                    wr(' disabled')

                wr(' value="' + item[0]['value'] + '"')
                if item[0]['checked']:
                    wr(' checked')                    
                wr('>')
                wr(item[0]['label'])

                wr('</input>')
                wr("</h3>")
                
        wr("<h2>" + form["postmessage"] + "</h2>")
        #wr("</table>")
        wr('</div>')
