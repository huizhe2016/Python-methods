# -*- coding: utf-8 -*-
#python version 2.7
#ip port scanning
#use socket scanning
#建议使用多进程不然会很浪费时间
import socket


class PortService(object):
    '''服务器端口检测及扫描(外部扫描65535个端口)'''
    def __init__(self,ip):
        self.ip = ip

    @staticmethod
    def detection(ip, port):
        '''检测ip 端口是否正常(return 0 correct,异常返回其它)'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            conn = s.connect_ex((ip, port))
            s.close()
            return conn
        except Exception,e:
            s.close()
            return e

    def scanning(self,port_type=None,**kwargs):
        '''扫描一个ip的所有端口'''
        scann_results = []
        for i in range(0,65536):
            status = PortService.detection(self.ip,i)
            scann_results.append([self.ip,status])
        return scann_results