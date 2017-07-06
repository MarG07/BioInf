genome_name="genome_annotation.gtf"

gene_minys_starts=[]
gene_minys_ends=[]
gene_minys_name=[]
gene_plys_starts=[]
gene_plys_ends=[]
gene_plys_name=[]

read_flags=[]
read_starts=[]
read_ends=[]

flag2=[]
pos2=[]
seq2=[]

with open(r'C:\Users\marin\Desktop\gene_counts\genome_annotation.gtf') as inp:
    for line in inp:
        gene_info=line.strip().split('\t')
        additional_info=line.strip().split('"')
        
        if gene_info[6]=='+':
            gene_plys_starts.append(int(gene_info[3]))
            gene_plys_ends.append(int(gene_info[4]))
            gene_plys_name.append(additional_info[5])
        else:
            gene_minys_starts.append(int(gene_info[3]))
            gene_minys_ends.append(int(gene_info[4]))
            gene_minys_name.append(additional_info[5])

def count_reads(filename):
    gene_count = {}
    for name in gene_plys_name:
        gene_count[name] = 0

    for name in gene_minys_name:
        gene_count[name] = 0
    
    with open(filename) as inp:
        plys_index = 0
        minys_index = 0
        for line in inp:
            if line[0]=='@':
                continue 
            gene_info=line.strip().split('\t')
            read_flag = int(gene_info[1])
            read_start = int(gene_info[3])
            read_end = int(gene_info[3])+len(gene_info[9])

            if read_flag & 4:
                continue
        
            if read_flag & 16:
                read_strand = '-'    
            else:
                read_strand = '+'

            if read_strand=='+':
                while plys_index<len(gene_plys_starts):
                    if gene_plys_starts[plys_index]-read_end>0:
                        break
                    elif read_start-gene_plys_ends[plys_index]>0:
                        plys_index+=1
                    else:
                        gene_count[gene_plys_name[plys_index]] += 1
                        break
                
            if read_strand=='-':
                while minys_index < len(gene_minys_starts):
                    if gene_minys_starts[minys_index]-read_end>0:
                        break
                    elif read_start-gene_minys_ends[minys_index]>0:
                        minys_index+=1
                    else:
                        gene_count[gene_minys_name[minys_index]] += 1
                        break

    return gene_count

count_reads(r'C:\Users\marin\Desktop\gene_counts\THYP2_22.sam')
count_reads(r'C:\Users\marin\Desktop\gene_counts\TNOR2_22.sam')
print(read_name,'\t',ref_name,'\t',result,'\t',read,'\t',read_quality,'\t',file=out)
