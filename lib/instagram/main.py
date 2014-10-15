#!/home/jonferrer/jonferrer.env/bin/python
""" Gets the most recent intagrams for instagram/@jonnyheadphones and saves to local redis """
import time
from instagram.client import InstagramAPI
import redis
from config import CLIENT_ID, USER_ID, REDIS_CONFIG

if __name__ == '__main__':
	# Get the last 5 instagrams
	recent_instagrams = []
	count = 5
	image_type = 'low_resolution'
	api = InstagramAPI(client_id=CLIENT_ID)
	recent_media, next_url = api.user_recent_media(user_id=USER_ID, count=count)
	
	redis_store = redis.Redis(REDIS_CONFIG['host'])
	
	for media in recent_media:
		recent_instagram = {
			'caption': media.caption.text,
			'created_time': time.mktime(media.created_time.timetuple()),
			'h': media.images[image_type].height,
			'like_count': media.like_count,
			#'likes': media.likes,
			'link': media.link,
			'url': media.images[image_type].url,
			'w': media.images[image_type].width,
		}
		recent_instagrams.append(recent_instagram)	

	redis_store.set(REDIS_CONFIG['instagram_recent_media_key'], recent_instagrams)

	# print redis_store.get(REDIS_CONFIG['instagram_recent_media_key'])
		

"""
Sample user_recent_media response:

{
  "pagination": {
    "next_url": "https:\/\/api.instagram.com\/v1\/users\/13458608\/media\/recent?count=5\u0026max_id=813324081242335076_13458608\u0026client_id=c0961096e20d423a87dfe27409f49bd6",
    "next_max_id": "813324081242335076_13458608"
  },
  "meta": {
    "code": 200
  },
  "data": [{
    "attribution": null,
    "tags": [],
    "location": {
      "latitude": 40.762283333,
      "name": "Ferrer's House of Pork",
      "longitude": -73.929695,
      "id": 360771126
    },
    "comments": {
      "count": 4,
      "data": [{
        "created_time": "1413151545",
        "text": "made with the haul from yesterday's excursion with @ericjhannon @aylee223 @jennisspecial to gravesend!",
        "from": {
          "username": "jonnyheadphones",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
          "id": "13458608",
          "full_name": "Jon Ferrer"
        },
        "id": "829897770083575551"
      }, {
        "created_time": "1413155083",
        "text": "Did you make the tortillas too? They look delish!",
        "from": {
          "username": "limorsuss",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_264541477_75sq_1394801610.jpg",
          "id": "264541477",
          "full_name": "Limor Suss"
        },
        "id": "829927450211805054"
      }, {
        "created_time": "1413156816",
        "text": "I was still full this morning!",
        "from": {
          "username": "aylee223",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_25325118_75sq_1399240025.jpg",
          "id": "25325118",
          "full_name": "Ali"
        },
        "id": "829941988793542640"
      }, {
        "created_time": "1413173785",
        "text": "@limorsuss nope, I don't have those tortilla making skills. picked up them up yesterday in BK",
        "from": {
          "username": "jonnyheadphones",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
          "id": "13458608",
          "full_name": "Jon Ferrer"
        },
        "id": "830084336315819809"
      }]
    },
    "filter": "Normal",
    "created_time": "1413151520",
    "link": "http:\/\/instagram.com\/p\/uEY28XOGU2\/",
    "likes": {
      "count": 27,
      "data": [{
        "username": "rescolar",
        "profile_picture": "http:\/\/photos-d.ak.instagram.com\/hphotos-ak-xpa1\/10449029_596613050437091_1815934341_a.jpg",
        "id": "344842545",
        "full_name": "Rhodin Escolar"
      }, {
        "username": "elad.gilo",
        "profile_picture": "http:\/\/photos-e.ak.instagram.com\/hphotos-ak-xpa1\/10513852_1432353100372164_1115814043_a.jpg",
        "id": "1413289343",
        "full_name": "Elad G"
      }, {
        "username": "newsum",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_9470092_75sq_1358740243.jpg",
        "id": "9470092",
        "full_name": "Shaun Newsum"
      }, {
        "username": "vladelena86",
        "profile_picture": "http:\/\/photos-e.ak.instagram.com\/hphotos-ak-xfa1\/10731878_731736783586004_1562032426_a.jpg",
        "id": "1369501745",
        "full_name": "Elena"
      }]
    },
    "images": {
      "low_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xaf1\/t51.2885-15\/10724743_611527648957343_1791921836_a.jpg",
        "width": 306,
        "height": 306
      },
      "thumbnail": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xaf1\/t51.2885-15\/10724743_611527648957343_1791921836_s.jpg",
        "width": 150,
        "height": 150
      },
      "standard_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xaf1\/t51.2885-15\/10724743_611527648957343_1791921836_n.jpg",
        "width": 640,
        "height": 640
      }
    },
    "users_in_photo": [],
    "caption": {
      "created_time": "1413151520",
      "text": "smoked pork shoulder tacos, homemade chipotle-tomato sauce",
      "from": {
        "username": "jonnyheadphones",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
        "id": "13458608",
        "full_name": "Jon Ferrer"
      },
      "id": "829897560527759092"
    },
    "type": "image",
    "id": "829897560125105462_13458608",
    "user": {
      "username": "jonnyheadphones",
      "website": "",
      "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
      "full_name": "Jon Ferrer",
      "bio": "",
      "id": "13458608"
    }
  }, {
    "attribution": null,
    "tags": [],
    "location": {
      "latitude": 40.720946,
      "name": "Yakitori TORA",
      "longitude": -73.996337,
      "id": 411878828
    },
    "comments": {
      "count": 4,
      "data": [{
        "created_time": "1412734911",
        "text": "@tolar",
        "from": {
          "username": "jonnyheadphones",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
          "id": "13458608",
          "full_name": "Jon Ferrer"
        },
        "id": "826402796012594288"
      }, {
        "created_time": "1412734959",
        "text": "!!",
        "from": {
          "username": "tolar",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_85055_75sq_1286941186.jpg",
          "id": "85055",
          "full_name": "Rob Haining"
        },
        "id": "826403194429531270"
      }, {
        "created_time": "1412735545",
        "text": "\u2757\ufe0f\u2757\ufe0f\u2757\ufe0f",
        "from": {
          "username": "kareny123",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_1144472_75sq_1334774120.jpg",
          "id": "1144472",
          "full_name": "kareny123"
        },
        "id": "826408113651869137"
      }, {
        "created_time": "1412736042",
        "text": "#zenballs",
        "from": {
          "username": "mikeodea",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_205295_75sq_1309690129.jpg",
          "id": "205295",
          "full_name": "Mike O'Dea"
        },
        "id": "826412283553408752"
      }]
    },
    "filter": "Normal",
    "created_time": "1412734891",
    "link": "http:\/\/instagram.com\/p\/t3-M-nOGVB\/",
    "likes": {
      "count": 23,
      "data": [{
        "username": "marizbee",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_1434475_75sq_1362317341.jpg",
        "id": "1434475",
        "full_name": "Mariz Badelles"
      }, {
        "username": "thebrendagenda",
        "profile_picture": "http:\/\/photos-a.ak.instagram.com\/hphotos-ak-xap1\/10299855_1387722191467256_508452850_a.jpg",
        "id": "47599958",
        "full_name": "thebrendagenda"
      }, {
        "username": "timryon",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_339622285_75sq_1366493138.jpg",
        "id": "339622285",
        "full_name": "Tim Ryon"
      }, {
        "username": "macaronijabroni",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_232824283_75sq_1394248795.jpg",
        "id": "232824283",
        "full_name": "macaronijabroni"
      }]
    },
    "images": {
      "low_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xfa1\/t51.2885-15\/10706873_1475355352725979_1048040157_a.jpg",
        "width": 306,
        "height": 306
      },
      "thumbnail": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xfa1\/t51.2885-15\/10706873_1475355352725979_1048040157_s.jpg",
        "width": 150,
        "height": 150
      },
      "standard_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xfa1\/t51.2885-15\/10706873_1475355352725979_1048040157_n.jpg",
        "width": 640,
        "height": 640
      }
    },
    "users_in_photo": [{
      "position": {
        "y": 0.3828125,
        "x": 0.346875
      },
      "user": {
        "username": "quintonma",
        "profile_picture": "http:\/\/photos-b.ak.instagram.com\/hphotos-ak-xap1\/926571_334784636698769_1311636806_a.jpg",
        "id": "931551",
        "full_name": "Quinton M\ud83c\udf5c"
      }
    }, {
      "position": {
        "y": 0.184375,
        "x": 0.71875
      },
      "user": {
        "username": "jennisspecial",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_304585438_75sq_1360472565.jpg",
        "id": "304585438",
        "full_name": "Jennifer Riegle"
      }
    }],
    "caption": {
      "created_time": "1412734891",
      "text": "onigiri meditation",
      "from": {
        "username": "jonnyheadphones",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
        "id": "13458608",
        "full_name": "Jon Ferrer"
      },
      "id": "826402628743750751"
    },
    "type": "image",
    "id": "826402627393185089_13458608",
    "user": {
      "username": "jonnyheadphones",
      "website": "",
      "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
      "full_name": "Jon Ferrer",
      "bio": "",
      "id": "13458608"
    }
  }, {
    "attribution": null,
    "tags": [],
    "location": {
      "latitude": 40.762283333,
      "name": "Ferrer's House of Pork",
      "longitude": -73.929695,
      "id": 360771126
    },
    "comments": {
      "count": 1,
      "data": [{
        "created_time": "1411959288",
        "text": "Saraaaaap",
        "from": {
          "username": "ext212",
          "profile_picture": "http:\/\/photos-e.ak.instagram.com\/hphotos-ak-xpa1\/10499086_1463762440540412_356095772_a.jpg",
          "id": "815889",
          "full_name": "cia b"
        },
        "id": "819896398927914707"
      }]
    },
    "filter": "Normal",
    "created_time": "1411951073",
    "link": "http:\/\/instagram.com\/p\/tgnMFxOGbS\/",
    "likes": {
      "count": 31,
      "data": [{
        "username": "ext212",
        "profile_picture": "http:\/\/photos-e.ak.instagram.com\/hphotos-ak-xpa1\/10499086_1463762440540412_356095772_a.jpg",
        "id": "815889",
        "full_name": "cia b"
      }, {
        "username": "szstone",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_24342387_75sq_1362875304.jpg",
        "id": "24342387",
        "full_name": "Suzanne Stone"
      }, {
        "username": "alzeidler",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_227036075_75sq_1373497090.jpg",
        "id": "227036075",
        "full_name": "alzeidler"
      }, {
        "username": "theoccho",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_5153933_75sq_1391181457.jpg",
        "id": "5153933",
        "full_name": "Chris Occhipinti"
      }]
    },
    "images": {
      "low_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xpf1\/t51.2885-15\/1171091_711514118956335_1659887458_a.jpg",
        "width": 306,
        "height": 306
      },
      "thumbnail": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xpf1\/t51.2885-15\/1171091_711514118956335_1659887458_s.jpg",
        "width": 150,
        "height": 150
      },
      "standard_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xpf1\/t51.2885-15\/1171091_711514118956335_1659887458_n.jpg",
        "width": 640,
        "height": 640
      }
    },
    "users_in_photo": [{
      "position": {
        "y": 0.86875,
        "x": 0.1421875
      },
      "user": {
        "username": "jennisspecial",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_304585438_75sq_1360472565.jpg",
        "id": "304585438",
        "full_name": "Jennifer Riegle"
      }
    }],
    "caption": {
      "created_time": "1411951073",
      "text": "bulalo! (aka the first time I've cooked filipino food in a while)",
      "from": {
        "username": "jonnyheadphones",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
        "id": "13458608",
        "full_name": "Jon Ferrer"
      },
      "id": "819827487326889726"
    },
    "type": "image",
    "id": "819827486823573202_13458608",
    "user": {
      "username": "jonnyheadphones",
      "website": "",
      "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
      "full_name": "Jon Ferrer",
      "bio": "",
      "id": "13458608"
    }
  }, {
    "attribution": null,
    "tags": [],
    "location": {
      "latitude": 40.746227143,
      "name": "Long Island City water view",
      "longitude": -73.958510534,
      "id": 229759650
    },
    "comments": {
      "count": 0,
      "data": []
    },
    "filter": "Normal",
    "created_time": "1411702358",
    "link": "http:\/\/instagram.com\/p\/tZMzWpuGaj\/",
    "likes": {
      "count": 10,
      "data": [{
        "username": "nfrand",
        "profile_picture": "http:\/\/photos-g.ak.instagram.com\/hphotos-ak-xaf1\/10601943_1533259366898062_1427718700_a.jpg",
        "id": "3315120",
        "full_name": "Nicole Frand"
      }, {
        "username": "ekzeid",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_415206201_75sq_1371012755.jpg",
        "id": "415206201",
        "full_name": "Emily Zeidler"
      }, {
        "username": "ryonlockhartphotography",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_298676700_75sq_1363549845.jpg",
        "id": "298676700",
        "full_name": "Sarah Lockhart"
      }, {
        "username": "frenchphonograph",
        "profile_picture": "http:\/\/photos-g.ak.instagram.com\/hphotos-ak-xfa1\/10611272_445524992254982_1721258896_a.jpg",
        "id": "25371135",
        "full_name": "Michael Domanic"
      }]
    },
    "images": {
      "low_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xaf1\/t51.2885-15\/10666107_341550442680000_534622897_a.jpg",
        "width": 306,
        "height": 306
      },
      "thumbnail": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xaf1\/t51.2885-15\/10666107_341550442680000_534622897_s.jpg",
        "width": 150,
        "height": 150
      },
      "standard_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xaf1\/t51.2885-15\/10666107_341550442680000_534622897_n.jpg",
        "width": 640,
        "height": 640
      }
    },
    "users_in_photo": [{
      "position": {
        "y": 0.7078125,
        "x": 0.2546875
      },
      "user": {
        "username": "gastronauts",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_1414939_75sq_1362783592.jpg",
        "id": "1414939",
        "full_name": "The Gastronauts"
      }
    }, {
      "position": {
        "y": 0.446875,
        "x": 0.4234375
      },
      "user": {
        "username": "jennisspecial",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_304585438_75sq_1360472565.jpg",
        "id": "304585438",
        "full_name": "Jennifer Riegle"
      }
    }],
    "caption": {
      "created_time": "1411702358",
      "text": "goodnight billboard",
      "from": {
        "username": "jonnyheadphones",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
        "id": "13458608",
        "full_name": "Jon Ferrer"
      },
      "id": "817741113496987252"
    },
    "type": "image",
    "id": "817741112918173347_13458608",
    "user": {
      "username": "jonnyheadphones",
      "website": "",
      "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
      "full_name": "Jon Ferrer",
      "bio": "",
      "id": "13458608"
    }
  }, {
    "attribution": null,
    "tags": [],
    "location": {
      "latitude": 40.762283333,
      "name": "Ferrer's House of Pork",
      "longitude": -73.929695,
      "id": 360771126
    },
    "comments": {
      "count": 2,
      "data": [{
        "created_time": "1411178778",
        "text": "Damn",
        "from": {
          "username": "aylee223",
          "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_25325118_75sq_1399240025.jpg",
          "id": "25325118",
          "full_name": "Ali"
        },
        "id": "813349006808212719"
      }, {
        "created_time": "1411180629",
        "text": "Where's my invite?",
        "from": {
          "username": "thisonespecifically",
          "profile_picture": "http:\/\/photos-f.ak.instagram.com\/hphotos-ak-xfa1\/10706633_1602509389976653_444071625_a.jpg",
          "id": "346864349",
          "full_name": "Ally Spier"
        },
        "id": "813364527763055831"
      }]
    },
    "filter": "Normal",
    "created_time": "1411175807",
    "link": "http:\/\/instagram.com\/p\/tJgfFVuGdk\/",
    "likes": {
      "count": 29,
      "data": [{
        "username": "vernaellaine",
        "profile_picture": "http:\/\/photos-a.ak.instagram.com\/hphotos-ak-xpa1\/926522_439010772903056_953928185_a.jpg",
        "id": "34809938",
        "full_name": "vernaellaine"
      }, {
        "username": "ryonlockhartphotography",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_298676700_75sq_1363549845.jpg",
        "id": "298676700",
        "full_name": "Sarah Lockhart"
      }, {
        "username": "e_matsuyama",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_9038994_75sq_1365195753.jpg",
        "id": "9038994",
        "full_name": "Emi"
      }, {
        "username": "sjs219",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_14785446_75sq_1332356109.jpg",
        "id": "14785446",
        "full_name": "sjs219"
      }]
    },
    "images": {
      "low_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xfa1\/t51.2885-15\/10707128_748505678520309_557083936_a.jpg",
        "width": 306,
        "height": 306
      },
      "thumbnail": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xfa1\/t51.2885-15\/10707128_748505678520309_557083936_s.jpg",
        "width": 150,
        "height": 150
      },
      "standard_resolution": {
        "url": "http:\/\/scontent-b.cdninstagram.com\/hphotos-xfa1\/t51.2885-15\/10707128_748505678520309_557083936_n.jpg",
        "width": 640,
        "height": 640
      }
    },
    "users_in_photo": [],
    "caption": {
      "created_time": "1411175807",
      "text": "romesco de peix",
      "from": {
        "username": "jonnyheadphones",
        "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
        "id": "13458608",
        "full_name": "Jon Ferrer"
      },
      "id": "813324081795983027"
    },
    "type": "image",
    "id": "813324081242335076_13458608",
    "user": {
      "username": "jonnyheadphones",
      "website": "",
      "profile_picture": "http:\/\/images.ak.instagram.com\/profiles\/profile_13458608_75sq_1321748669.jpg",
      "full_name": "Jon Ferrer",
      "bio": "",
      "id": "13458608"
    }
  }]
}

"""
