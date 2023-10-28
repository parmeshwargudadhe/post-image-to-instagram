import json
import requests

def publish_image():
    access_token="ACCESS-TOKEN"
    ig_user_id="INSTAGRAM-ID"
    image_url="IMAGE-URL"
    post_url='https://graph.facebook.com/v18.0/{}/media'.format(ig_user_id)
    
    payload={
        'image_url': image_url,
        'caption': "Instagram post using Graph API",
        'access_token': access_token
    }

    r=requests.post(post_url, data=payload)
    print(r.text)
    print('Media Uploaded Successfully')

    results=json.loads(r.text)

    if 'id' in results:
        creation_id=results['id']
        second_url='https://graph.facebook.com/v18.0/{}/media_publish'.format(ig_user_id)
        second_payload={
            'creation_id':creation_id,
            'access_token':access_token
        }

        r=requests.post(second_url, data=second_payload)
        print(r.text)
        print('Media Posted Successfully')
    else:
        print('Image posting on Instagram is not possible')

# Call the function
publish_image()