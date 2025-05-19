# 🧠 Algorithm Practice

This repository contains my solutions to algorithm problems from various online judges.

## Platforms
- [Baekjoon Online Judge](https://www.acmicpc.net)
- [Programmers](https://programmers.co.kr)
- [LeetCode](https://leetcode.com) (planned)

## Structure

coin-trading-bot/
├── agents/         # 강화학습 에이전트 (DQN, PPO 등)
├── config/         # 설정 파일
├── data/           # 비트코인 시세 데이터 처리
├── envs/           # 트레이딩 환경
├── models/         # 정책/가치 네트워크 등
├── scripts/        # 학습, 평가, 실거래 실행 스크립트
├── train.py        # 학습 entrypoint
├── run.py          # 실거래/추론 entrypoint
├── .gitignore
├── .dockerignore
└── README.md
