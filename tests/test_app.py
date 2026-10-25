
import unittest
from server.app import app


class AccessibilityAuditTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Accessibility Audit API is running",
            response.data
        )

    def test_findings_route(self):
        response = self.client.get("/api/findings")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(len(data), 5)

    def test_findings_have_required_fields(self):
        response = self.client.get("/api/findings")
        data = response.get_json()

        for finding in data:
            self.assertIn("id", finding)
            self.assertIn("title", finding)
            self.assertIn("priority", finding)
            self.assertIn("category", finding)


if __name__ == "__main__":
    unittest.main()
