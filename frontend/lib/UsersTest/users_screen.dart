import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:http/http.dart';
import 'package:flutter/material.dart';

import 'package:frontend/UsersTest/user.dart';

class UsersScreen extends StatefulWidget {
  const UsersScreen({Key? key}) : super(key: key);

  @override
  State<UsersScreen> createState() => _UsersScreenState();
}

class _UsersScreenState extends State<UsersScreen> {
  late Future<List<User>> users;
  final usersListKey = GlobalKey<_UsersScreenState>();

  @override
  void initState() {
    super.initState();
    users = getUsersList();
  }

  Future<List<User>> getUsersList() async {
    final response =
        await http.get(Uri.parse("http://127.0.0.1:8000/api/users/"));

    final items = json.decode(response.body).cast<Map<String, dynamic>>();
    List<User> users = items.map<User>((json) {
      return User.fromJson(json);
    }).toList();

    return users;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: usersListKey,
      appBar: AppBar(
        title: Text('Employee List'),
      ),
      body: Center(
        child: FutureBuilder<List<User>>(
          future: users,
          builder: (BuildContext context, AsyncSnapshot snapshot) {
            // By default, show a loading spinner.
            if (!snapshot.hasData) return CircularProgressIndicator();
            // Render employee lists
            return ListView.builder(
              itemCount: snapshot.data.length,
              itemBuilder: (BuildContext context, int index) {
                var data = snapshot.data[index];
                return Card(
                  child: ListTile(
                    leading: Icon(Icons.person),
                    title: Text(
                      data.full_name,
                      style: TextStyle(fontSize: 20),
                    ),
                  ),
                );
              },
            );
          },
        ),
      ),
    );
  }
}
