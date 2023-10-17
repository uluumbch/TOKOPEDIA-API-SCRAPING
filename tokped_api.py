import requests
import pandas as pd

url = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'

headers = {
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Tkpd-UserId': '0',
    'X-Version': 'c326edb',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
     'Referer': 'https://www.tokopedia.com/',
    'X-Source': 'tokopedia-lite',
    'x-device': 'desktop-0.0',
    'X-Tkpd-Lite-Service': 'zeus',
    'sec-ch-ua-platform': '"Windows"'
}
keyword = 'botol minum' # change this
DATA = {
    'url' : [],
    'name' : [],
    'price' : [],
    'imageUrl' : [],
    'shopName' : [],
    'shopCity' : [],
    'rating' : [],
    'countReview' : [],
    'categoryName' : []
}
for i in range(1, 101):
    data = '[{"operationName":"SearchProductQueryV4","variables":{"params":"device=desktop&navsource=&ob=23&page='+str(i)+'&q='+keyword+'&related=true&rows=60&safe_search=false&scheme=https&shipping=&show_adult=false&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start='+ str((i - 1) * 60) +'&topads_bucket=true&unique_id=258586f31adbdb2d6acf02eac6262d18&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m"},"query":"query SearchProductQueryV4($params: String!) {\\n  ace_search_product_v4(params: $params) {\\n    header {\\n      totalData\\n      totalDataText\\n      processTime\\n      responseCode\\n      errorMessage\\n      additionalParams\\n      keywordProcess\\n      componentId\\n      __typename\\n    }\\n    data {\\n      banner {\\n        position\\n        text\\n        imageUrl\\n        url\\n        componentId\\n        trackingOption\\n        __typename\\n      }\\n      backendFilters\\n      isQuerySafe\\n      ticker {\\n        text\\n        query\\n        typeId\\n        componentId\\n        trackingOption\\n        __typename\\n      }\\n      redirection {\\n        redirectUrl\\n        departmentId\\n        __typename\\n      }\\n      related {\\n        position\\n        trackingOption\\n        relatedKeyword\\n        otherRelated {\\n          keyword\\n          url\\n          product {\\n            id\\n            name\\n            price\\n            imageUrl\\n            rating\\n            countReview\\n            url\\n            priceStr\\n            wishlist\\n            shop {\\n              shopId: id\\n              city\\n              isOfficial\\n              isPowerBadge\\n              __typename\\n            }\\n            ads {\\n              adsId: id\\n              productClickUrl\\n              productWishlistUrl\\n              shopClickUrl\\n              productViewUrl\\n              __typename\\n            }\\n            badges {\\n              title\\n              imageUrl\\n              show\\n              __typename\\n            }\\n            ratingAverage\\n            labelGroups {\\n              position\\n              type\\n              title\\n              url\\n              __typename\\n            }\\n            componentId\\n            warehouseIdDefault\\n            __typename\\n          }\\n          componentId\\n          __typename\\n        }\\n        __typename\\n      }\\n      suggestion {\\n        currentKeyword\\n        suggestion\\n        suggestionCount\\n        instead\\n        insteadCount\\n        query\\n        text\\n        componentId\\n        trackingOption\\n        __typename\\n      }\\n      products {\\n        id\\n        name\\n        ads {\\n          adsId: id\\n          productClickUrl\\n          productWishlistUrl\\n          productViewUrl\\n          __typename\\n        }\\n        badges {\\n          title\\n          imageUrl\\n          show\\n          __typename\\n        }\\n        category: departmentId\\n        categoryBreadcrumb\\n        categoryId\\n        categoryName\\n        countReview\\n        customVideoURL\\n        discountPercentage\\n        gaKey\\n        imageUrl\\n        labelGroups {\\n          position\\n          title\\n          type\\n          url\\n          __typename\\n        }\\n        originalPrice\\n        price\\n        priceRange\\n        rating\\n        ratingAverage\\n        shop {\\n          shopId: id\\n          name\\n          url\\n          city\\n          isOfficial\\n          isPowerBadge\\n          __typename\\n        }\\n        url\\n        wishlist\\n        sourceEngine: source_engine\\n        warehouseIdDefault\\n        __typename\\n      }\\n      violation {\\n        headerText\\n        descriptionText\\n        imageURL\\n        ctaURL\\n        ctaApplink\\n        buttonText\\n        buttonType\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}]'
    response = requests.post(url, headers=headers, data=data).json()

    hasil_data = response[0]['data']['ace_search_product_v4']['data']['products']

    print('Page', i)
    print('Jumlah data', len(hasil_data))

    if len(hasil_data) == 0:
        print('Data habis')
        break
    for data in hasil_data:
        DATA['url'].append(data['url'])
        DATA['name'].append(data['name'])
        DATA['price'].append(data['price'])
        DATA['imageUrl'].append(data['imageUrl'])
        DATA['shopName'].append(data['shop']['name'])
        DATA['shopCity'].append(data['shop']['city'])
        DATA['rating'].append(data['rating'])
        DATA['countReview'].append(data['countReview'])
        DATA['categoryName'].append(data['categoryName'])
        sells = '0'
        for label in data['labelGroups']:
            if 'terjual' in label['title']:
                sells = label['title']
                break
        DATA['sells'].append(sells)
        # print(data['url'])
        # print(data['name'])
        # print(data['price'])
        # print(data['imageUrl'])
        # print(data['shop']['name'])
        # print(data['shop']['city'])
        # print(data['rating'])
        # print(data['countReview'])
        # print(data['categoryName'])

df = pd.DataFrame(DATA)

with open('data_produk.csv', 'w', encoding='utf-8', newline='') as f:
    f.write(df.to_csv(index=False))
print('Selesai')