CREATE TABLE IF NOT EXISTS chat_records (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    type INT NOT NULL,
    content TEXT NOT NULL,
    title VARCHAR(255),
    creator_id VARCHAR(255) NOT NULL,
    assigned_to_id VARCHAR(255),
    create_time TIMESTAMP NOT NULL,
    update_time TIMESTAMP,
    INDEX idx_creator_id (creator_id),
    INDEX idx_assigned_to_id (assigned_to_id),
    INDEX idx_create_time (create_time),
    INDEX idx_type (type)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO chat_records (type, content, title, creator_id, assigned_to_id, create_time, update_time)
VALUES
(1, '这是第一条聊天记录的内容', '第一条记录', 'user123', 'user456', NOW(), NOW()),
(2, '这是第二条聊天记录的内容', '第二条记录', 'user124', 'user457', NOW(), NOW()),
(1, '这是第三条聊天记录的内容', '第三条记录', 'user123', 'user458', NOW(), NOW()),
(3, '这是第四条聊天记录的内容', '第四条记录', 'user125', 'user456', NOW(), NOW()),
(1, '这是第五条聊天记录的内容', '第五条记录', 'user126', 'user459', NOW(), NOW());

