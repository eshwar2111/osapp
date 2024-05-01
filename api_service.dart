import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<void> registerUser(String username, String password) async {
    final response = await http.post(
      Uri.parse('http://localhost:5000'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'username': username,
        'password': password,
      }),
    );

    if (response.statusCode == 200) {
      print('User registered successfully');
    } else {
      print('Failed to register user');
    }
  }

  static Future<void> loginUser(String username, String password) async {
    final response = await http.post(
      Uri.parse('http://your_backend_url/login'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'username': username,
        'password': password,
      }),
    );

    if (response.statusCode == 200) {
      print('User logged in successfully');
    } else {
      print('Failed to login');
    }
  }
}
