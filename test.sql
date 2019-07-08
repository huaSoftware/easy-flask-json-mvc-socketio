/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 08/07/2019 09:05:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ht_comments
-- ----------------------------
DROP TABLE IF EXISTS `ht_comments`;
CREATE TABLE `ht_comments`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `msg` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '评论内容',
  `user_id` int(10) UNSIGNED NULL DEFAULT NULL COMMENT '用户id',
  `article_id` int(10) UNSIGNED NOT NULL,
  `add_time` int(11) UNSIGNED NOT NULL COMMENT '添加时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 189 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ht_img_shard
-- ----------------------------
DROP TABLE IF EXISTS `ht_img_shard`;
CREATE TABLE `ht_img_shard`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `imgString` text CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `index` int(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for ht_suggest
-- ----------------------------
DROP TABLE IF EXISTS `ht_suggest`;
CREATE TABLE `ht_suggest`  (
  `add_time` int(13) NOT NULL,
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `users_id` int(11) NOT NULL,
  `message` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 312313 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ht_users
-- ----------------------------
DROP TABLE IF EXISTS `ht_users`;
CREATE TABLE `ht_users`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `remember_token` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `created_at` int(13) NULL DEFAULT NULL,
  `updated_at` int(13) NULL DEFAULT NULL,
  `url_path` varchar(300) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `real_path` varchar(300) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `users_email_unique`(`email`) USING BTREE,
  UNIQUE INDEX `users_tel_unique`(`tel`) USING BTREE,
  UNIQUE INDEX `users_name_unique`(`name`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 34 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
