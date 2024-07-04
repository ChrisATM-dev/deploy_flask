select * from posts;

select * from users;

select * from comments;

select posts.*, users.first_name as user_name from posts join users where posts.user_id = users.id;

select comments.*, users.first_name as user_name from comments join users on comments.user_id = users.id where comments.post_id = 1;


