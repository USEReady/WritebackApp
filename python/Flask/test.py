try:
    import unittest
    from main import app
    import requests

    class FlaskTest(unittest.TestCase):
    #check response 400 or 404 not
        def test_index(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            statuscode = response.status_code
            self.assertEqual(statuscode,404)

        def test_index1(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            statuscode = response.status_code
            self.assertNotAlmostEqual(statuscode,400)    

        #check if content return is application/json
        def test_index_content(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            self.assertEqual(response.content_type, "application/json")

        #check for the data return 
        def test_index_data(self):
            tester = app.test_client(self)
            response = tester.get("/fo")
            self.assertFalse(b'Message' in response.data)
# #here we check api 
# class ApiTest(unittest.TestCase):
#     API_PORT=9443
#     def test_get_all_forecast(self):
#         r = requests.get(API_PORT)
#         self.assertEqual(r.status_code,200)    


except Exception as e:
    print("some moudles are missing {}".format(e))


if __name__ == "__main__":
    unittest.main()



