# if any of the actors orginally did not have postcodes,
# read in the manually searched postcodes
# if 'Export_LMA_actors_without_postcode.xlsx' in os.listdir(priv_folder + PART1):
#     LMA_actors_w_postcode = pd.read_excel(priv_folder + INPUT + 'Input_actors_without_postcode.xlsx'.format(scope))
#
#     # check if actor file is older than the postcode file
#     # if not, give a warning as indexes might not match
#     t1 = os.path.getctime(priv_folder + PART1 + 'Export_LMA_actors.xlsx')
#     t2 = os.path.getctime(priv_folder + INPUT + 'Input_actors_without_postcode.xlsx')
#
#     if t1 > t2:
#         print 'WARNING! Your part1 exports are newer than other input files,'
#         print 'make sure they are all up to date'
#
#     LMA_actors.update(LMA_actors_w_postcode, overwrite=False)
#     no_postcode = LMA_actors[LMA_actors['Postcode'] == np.NaN]
#     if len(no_postcode.index) > 0:
#         print 'WARNING! Not all LMA actors have a postcode,',
#         print 'this will result in unexpected matching behaviour'
