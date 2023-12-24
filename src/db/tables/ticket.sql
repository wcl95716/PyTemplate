-- 删除表（如果它已经存在）
DROP TABLE IF EXISTS ticket;

-- 创建表格
CREATE TABLE IF NOT EXISTS ticket (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    status INT,
    priority INT,
    type INT,
    title TEXT,
    content TEXT,
    assigned_to_id VARCHAR(100),
    creator_id VARCHAR(100),
    create_time DATETIME,
    update_time DATETIME,
    extended_field JSON,
    uu_id VARCHAR(100),
    INDEX idx_ticket_status (status),
    INDEX idx_ticket_priority (priority),
    INDEX idx_create_time (create_time),
    INDEX idx_ticket_assigned_to_id (assigned_to_id),
    INDEX idx_ticket_creator_id (creator_id),
    INDEX idx_ticket_type (type),
    INDEX idx_ticket_uuid (uu_id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- 插入数据
-- 插入数据，其中 key_id 字段为空
INSERT INTO ticket ( status, priority, type, title, content, assigned_to_id, creator_id, create_time, update_time)
VALUES 
    ( 1, 1, 1, 'test1', 'content1', '1', '1', '2020-01-01 01:00:00', '2020-01-01 02:00:00'),
    ( 2, 1, 1, 'test2', 'content2', '2', '2', '2020-01-02 00:00:00', '2020-01-02 00:00:00'),
    (3, 1, 1, 'test3', 'content3', '3', '3', '2020-01-03 00:00:00', '2020-01-03 00:00:00'),
    ( 1, 1, 1, '阿斯顿', '这是第一条聊天记录的内容', '1', '1', '2020-01-01 01:00:00', '2020-01-01 02:00:00'),
    ( 2, 1, 1, '我企鹅', '这是第一条聊天记录的内容', '2', '2', '2020-01-02 00:00:00', '2020-01-02 00:00:00'),
    (3, 1, 1, '自行车', '这是第一条聊天记录的内容', '3', '3', '2020-01-03 00:00:00', '2020-01-03 00:00:00');





