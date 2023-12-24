-- 删除表（如果它已经存在）
DROP TABLE IF EXISTS notification_task;

-- 创建表格
CREATE TABLE IF NOT EXISTS notification_task (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    notification_type VARCHAR(255) NOT NULL,
    destination JSON,  -- assuming JSON format or similar
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    priority INTEGER NOT NULL,
    status INTEGER NOT NULL,
    type VARCHAR(255) NOT NULL,
    creator_id VARCHAR(255),
    assigned_to_id VARCHAR(255) NOT NULL,
    create_time TIMESTAMP NOT NULL,
    update_time TIMESTAMP NOT NULL,
    INDEX idx_status (status),
    INDEX idx_priority (priority),
    INDEX idx_create_time (create_time),
    INDEX idx_assigned_to_id (assigned_to_id),
    INDEX idx_creator_id (creator_id),
    INDEX idx_notification_type (notification_type)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
