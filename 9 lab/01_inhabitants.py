#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

print(f"В комнате room_1 живут: {', '.join(room_1.folks)}")
print(f"В комнате room_2 живет: {', '.join(room_2.folks)}")