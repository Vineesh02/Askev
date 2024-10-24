from openai import OpenAI

f = open('apiKey.bin', 'r')
apiKey = f.read()
client = OpenAI(api_key=apiKey)
f.close()

def conChat():
    conChat.previous_response = None 
    while True:
        prompt = input(" ~ ")
        messages = [
            {"role": "system", "content": '''You are a helpful Whatsapp Business assistant, that understands & texts tamil language via English text
             these are the following products listed in your store:
             [['Product ',
                'Price / Rate',
                'color available ',
                'Image url',
                'Description',
                'Brand'],
            ["Symbol Premium Men's Wrinkle-Resistant Regular Fit Cotton Formal Shirt",
            'Rs. 1,399',
            'Black, Grey, Bottle Green, Dark Grey,Dark Purple',
            'https://m.media-amazon.com/images/I/71-GakBLxWL._SY879_.jpg',
            'A solid color formal shirt in twill weave with Wrinkle-Resistant finish Moisture Cure Treatment for better BreathabilitySemi Cutaway Collar, for a sharp look. ',
            'Symbol Premium'],
            ["Urbano Fashion Men's Regular Fit Washed Full Sleeve Denim Jacket",
            'Rs. 1,249',
            'Dark, Blue, Light Grey, Black',
            'https://m.media-amazon.com/images/I/71uoGwRbbiL._SX679_.jpg',
            'Stylish Blue Denim Jacket; Trendy Heavy Washed Pattern, 100% Denim Cotton Fabric ; Regular Fit ; Buttoned Full-Front Opening ; Slim Collar, 2 Dummy Chest Pockets with Flap and 2 Front Welt Pockets ; Regular Length ; Buttoned Cuff Perfect for Winter Season, Cool Casual, Evening & Holiday Wear\nWash Care - Mild Wash ; Wash dark colors separately ; Disclaimer - There may be slight variation in shade and colour due to photographic effects and monitor settings',
            'Urbano Fashion'],
            ["OFF LIMITS Men's STUSSYY Big and Tall Sports Shoes",
            'Rs. 2,799',
            'Grey',
            'https://m.media-amazon.com/images/I/61HfyeejxgL._SY695_.jpg',
            'Phylon TPR sole provides traction and grip over varied surfaces, The upper has a PU base and a super, soft lining for added comfort., Best recommended for running, training, any sports activity,, Lace Up Closure make it easy to wear',
            'OFF LIMITS'],
            ["Peter England Men's Solid Super Slim Fit Front Knit Trouser",
            'Rs. 1,099',
            'Grey, Black',
            'https://m.media-amazon.com/images/I/61OZ6kPXbzL._SY879_.jpg',
            'Lycra Comfort is a fabric technology that combines Lycra fibers with other materials such as cotton for enhanced stretch, flexibility, and comfort. Premium Blends - Meticulously crafted from a blend of high-quality materials, these trousers offer a perfect balance of style and functionality. 4 Way Stretch - Designed to revolutionize your wardrobe with unmatched comfort and flexibility. Crafted with precision and style in mind, these pants are engineered to move seamlessly with your body in every direction.\nSlim Fit Solid',
            'Peter England'],
            ['Casio Vintage A158WA-1DF Black Digital Dial Silver Stainless Steel Band D011',
            'Rs. 1,525',
            'Silver',
            'https://m.media-amazon.com/images/I/61ybeKQto8L._SY879_.jpg',
            'Occasion : Casual,Case Material : Others,Case Diameter : 38 mm, Dispay Type : Analog ,Warranty : 1 year',
            'Casio'],
            ['UNBEATABLE Men s Running Shorts?Workout Running Shorts for Men Gym Yoga Outdoor Sports Shorts',
            'Rs. 280',
            'G.ARMY, D.GREY, L.GREY',
            'https://m.media-amazon.com/images/I/911s5YiF+pL._SY879_.jpg',
            'INTIMATE DESIGN - Adjustable drawstring for greater waist comfort, the standard length is more convenient for leg movement. Pocket and towel ring design, convenient to put your personal belongings when you exercise. Zipper design, higher security, towel hanging on the towel ring, ready to use. FABRIC FEATURES- High elastic fabric is more convenient for sports. Quick-drying and breathable fabric can quickly drain sweat and keep dry so that you can keep comfortable during or after exercise.\n',
            'UNBEATABLE']]'''},
            {"role": "user", "content": prompt}
        ]
        if conChat.previous_response:
            messages.append(conChat.previous_response)
        chat_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        conChat.previous_response = {"role": "assistant", "content": chat_response.choices[0].message.content}
        print("---> ", chat_response.choices[0].message.content)

conChat()