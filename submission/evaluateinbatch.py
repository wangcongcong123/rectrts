file_thre_dict = {'BasicJaccard/threshold-00': 0.0, 'BasicJaccard/threshold-002': 0.02,
                  'BasicJaccard/threshold-004': 0.04, 'BasicJaccard/threshold-006': 0.06,
                  'BasicJaccard/threshold-008': 0.08, 'BasicJaccard/threshold-01': 0.1,
                  'BasicJaccard/threshold-012': 0.12, 'BasicJaccard/threshold-014': 0.14,
                  'BasicJaccard/threshold-016': 0.16, 'BasicJaccard/threshold-018': 0.18,
                  'BasicJaccard/threshold-02': 0.2, 'BasicJaccard/threshold-022': 0.22,
                  'BasicJaccard/threshold-024': 0.24, 'BasicJaccard/threshold-026': 0.26,
                  'BasicJaccard/threshold-028': 0.28, 'BasicJaccard/threshold-03': 0.3,
                  'BasicJaccard/threshold-032': 0.32, 'BasicJaccard/threshold-034': 0.34,
                  'BasicJaccard/threshold-036': 0.36, 'BasicJaccard/threshold-038': 0.38,
                  'BasicJaccard/threshold-04': 0.4, 'BasicJaccard/threshold-042': 0.42,
                  'BasicJaccard/threshold-044': 0.44, 'BasicJaccard/threshold-046': 0.46,
                  'BasicJaccard/threshold-048': 0.48, 'BasicJaccard/threshold-05': 0.5,
                  'BasicJaccard/threshold-052': 0.52, 'BasicJaccard/threshold-054': 0.54,
                  'BasicJaccard/threshold-056': 0.56, 'BasicJaccard/threshold-058': 0.58,
                  'BasicJaccard/threshold-06': 0.6, 'BasicJaccard/threshold-062': 0.62,
                  'BasicJaccard/threshold-064': 0.64, 'BasicJaccard/threshold-066': 0.66,
                  'BasicJaccard/threshold-068': 0.68, 'BasicJaccard/threshold-07000000000000001': 0.70,
                  'BasicJaccard/threshold-072': 0.72, 'BasicJaccard/threshold-074': 0.74,
                  'BasicJaccard/threshold-076': 0.76, 'BasicJaccard/threshold-078': 0.78,
                  'BasicJaccard/threshold-08': 0.80, 'BasicJaccard/threshold-08200000000000001': 0.82,
                  'BasicJaccard/threshold-084': 0.84, 'BasicJaccard/threshold-086': 0.86,
                  'BasicJaccard/threshold-088': 0.88, 'BasicJaccard/threshold-09': 0.90}

# print("\t".join(["Threshold", "run", "topic", "relevant", "redundant", "not_relevant",
#                  "online_utility(strict)", "online_utility(lenient)",
#                  "unjudged", "total_length", "mean_latency", "median_latency"]))
# import rts2017mobileeval as me
# for k,v in file_thre_dict.items():
#     print(str(v)+"\t"+me.evaluate(k))

import rts2017batchAeval as bae

print("\t".join(["Threshold", "runtag", "topic",
    "EGp", "EG1", "nCGp", "nCG1",
    "GMP.33", "GMP.50", "GMP.66",
    "mean_latency", "median_latency",
    "total_length"]))

for k,v in file_thre_dict.items():
    print(str(v)+"\t"+bae.evaluate(k))
