class User {
  final String slug;
  final String full_name;
  final String address;
  final String telegram_id;

  User(
      {required this.slug,
      required this.full_name,
      required this.address,
      required this.telegram_id});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      slug: json['slug'],
      full_name: json['full_name'],
      address: json['address'],
      telegram_id: json['telegram_id'],
    );
  }
  Map<String, dynamic> toJson() => {
        'slug': slug,
        'full_name': full_name,
        'address': address,
        'telegram_id': telegram_id,
      };
}
