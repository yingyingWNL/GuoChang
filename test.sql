-- 用户表
CREATE TABLE user (
    userID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NULL DEFAULT NULL,
    email VARCHAR(255) NULL DEFAULT NULL,
    password VARCHAR(255) NULL,
    mobilePhoneNumber VARCHAR(11) NULL,
);

-- 文章表
CREATE TABLE post (
    postID INT AUTO_INCREMENT PRIMARY KEY,
    authorID INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NULL,
    publishTime TIMESTAMP NOT NULL,
    FOREIGN KEY (AuthorID) REFERENCES user(UserID)
);

-- 评论表
CREATE TABLE comment (
    commentID INT AUTO_INCREMENT PRIMARY KEY,
    postID INT NOT NULL,
    authorID INT NOT NULL,
    content TEXT NOT NULL,
    commentTime TIMESTAMP NOT NULL,
    FOREIGN KEY (PostID) REFERENCES post(PostID),
    FOREIGN KEY (AuthorID) REFERENCES user(UserID)
);
